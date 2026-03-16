"""
Gerenciamento de alunos (frontend helpers) para Project-CK.

Este módulo fornece funções Streamlit reutilizáveis para:
- mostrar um formulário de edição de aluno preenchido (`show_edit_student_form`)
- confirmar e executar a exclusão de um aluno com confirmação (`confirm_delete_student`)

Observação: As funções usam `app.Utils.api_connector` para chamar a API.
Use essas funções a partir de um app Streamlit existente, fornecendo o `token` JWT válido.
"""
from typing import Callable
import streamlit as st
from app.Utils import api_connector


def show_edit_student_form(student: dict, token: str):
    """Exibe um formulário de edição para o aluno fornecido.

    Args:
        student: dicionário com os dados do aluno (deve conter ao menos '_id').
        token: JWT Bearer token para autorização nas chamadas à API.
    """
    if token is None or token == '':
        st.error('Token de autenticação ausente. Faça login antes de editar alunos.')
        return

    student_id = str(student.get('_id'))
    nome_default = student.get('nome', '')
    email_default = student.get('email', '')
    turma_default = str(student.get('turma_id') or student.get('class_id') or '')

    with st.form(key=f'edit_student_{student_id}'):
        nome = st.text_input('Nome', value=nome_default)
        email = st.text_input('Email', value=email_default)
        turma_id = st.text_input('Turma ID', value=turma_default, help='ID da turma (ObjectId)')

        submit = st.form_submit_button('Salvar alterações')
        if submit:
            payload = {
                'nome': nome,
                'email': email,
            }
            if turma_id:
                payload['turma_id'] = turma_id

            with st.spinner('Salvando alterações...'):
                try:
                    resp = api_connector.update_student(token, student_id, payload)
                except Exception as e:
                    st.error(f'Erro ao conectar com a API: {e}')
                    return

            if resp.status_code in (200, 201):
                st.success('Aluno atualizado com sucesso.')
            else:
                try:
                    data = resp.json()
                    st.error(f"Erro: {resp.status_code} - {data.get('message')}")
                except Exception:
                    st.error(f'Erro inesperado: {resp.status_code} - {resp.text}')


def confirm_delete_student(student_id: str, token: str, on_success: Callable[[], None] = None):
    """Mostra botão/expander para confirmar e executar a exclusão de um aluno.

    Args:
        student_id: ID do aluno a ser removido.
        token: JWT para autorização.
        on_success: callback opcional chamado após remoção bem-sucedida (por exemplo: recarregar lista).
    """
    if token is None or token == '':
        st.error('Token de autenticação ausente. Faça login antes de excluir alunos.')
        return

    # Botão principal (mostrado na linha do aluno)
    if st.button('🗑️ Deletar aluno', key=f'delete_{student_id}'):
        with st.expander('Confirmar exclusão'):
            st.warning('Aviso: esta ação é irreversível. Confirme para excluir o aluno permanentemente.')
            if st.button('Confirmar exclusão', key=f'confirm_delete_{student_id}'):
                with st.spinner('Removendo aluno...'):
                    try:
                        resp = api_connector.delete_student(token, student_id)
                    except Exception as e:
                        st.error(f'Erro ao conectar com a API: {e}')
                        return

                if resp.status_code == 200:
                    st.success('Aluno removido com sucesso.')
                    if on_success:
                        try:
                            on_success()
                        except Exception as e:
                            st.error(f'Erro no callback on_success: {e}')
                else:
                    try:
                        data = resp.json()
                        st.error(f"Erro: {resp.status_code} - {data.get('message')}")
                    except Exception:
                        st.error(f'Erro inesperado: {resp.status_code} - {resp.text}')
