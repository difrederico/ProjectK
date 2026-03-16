# 🚀 Guia Rápido de Início - Project-CK

## ⚡ Início Rápido (2 minutos)

### 1. Inicie o Backend
```powershell
cd "C:\Users\ACER\Desktop\GRADUAÇÃO I.A\2º Periodo\Pi\Project-CKV2.0\project-ck-backend"
docker-compose up
```

Aguarde até ver: `* Running on http://0.0.0.0:5001`

### 2. Inicie o Frontend
```powershell
cd "C:\Users\ACER\Desktop\GRADUAÇÃO I.A\2º Periodo\Pi\Project-CK3.0\project-ck"
streamlit run app.py
```

Aguarde abrir o navegador automaticamente!

### 3. Faça Login

Use uma das contas de teste:
- **Email**: `ana.sofia@aluno.dev`
- **Senha**: `senha123`

### 4. Pronto! 🎉

Agora você pode:
- ✅ Ver seu desempenho no Dashboard
- ✅ Fazer atividades educativas
- ✅ Visualizar relatórios personalizados

---

## 🔧 Troubleshooting Rápido

### Problema: Backend não inicia
**Solução**: Verifique se o Docker está rodando e a porta 5001 está livre

### Problema: Frontend não conecta à API
**Solução**: Verifique se o backend está rodando em http://localhost:5001

### Problema: Erro de autenticação
**Solução**: Verifique se está usando as credenciais corretas (email, não usuário)

---

## 📚 Próximos Passos

1. Leia `INTEGRACAO.md` para detalhes técnicos
2. Explore os módulos em `modules/`
3. Veja a documentação da API em http://localhost:5001/docs

---

## 🆘 Precisa de Ajuda?

- Documentação completa: Veja `README.md`
- Integração API: Veja `INTEGRACAO.md`
- Problemas técnicos: Verifique os logs do terminal
