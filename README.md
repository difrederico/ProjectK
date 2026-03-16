# Project-CK

Sistema de monitoramento e suporte para crianças neurodivergentes em ambiente escolar, utilizando IoT, Machine Learning e análise de dados em tempo real.

## Visão Geral

O Project-CK é uma plataforma integrada que combina:

- **Pulseira IoT (M5Stack)**: Coleta dados biométricos (batimentos cardíacos, temperatura, movimento)
- **Backend Flask**: API REST para gerenciamento de dados, alertas e autenticação
- **Frontend Streamlit**: Interface para professores e pais acompanharem os alunos
- **Machine Learning**: Modelo de classificação para detecção de crises

## Estrutura do Projeto

```
Project-CK/
├── project-ck-backend/       # API Flask + MongoDB
├── project-ck-front-end/     # Interface Streamlit
├── project-ck-pulseira-m5stack/  # Firmware da pulseira IoT
└── docs/                    # Documentação e análise de dados
```

## Tecnologias

| Componente | Tecnologias |
|------------|-------------|
| Backend | Python, Flask, MongoDB, Redis, MQTT |
| Frontend | Python, Streamlit, Plotly |
| IoT | MicroPython, M5Stack StickC Plus2 |
| ML | Scikit-learn, Pandas, Joblib |
| Infra | Docker, Docker Compose |

## Início Rápido

### 1. Backend (Docker)

```bash
cd project-ck-backend
cp .env.example .env
# Edite .env com suas configurações
docker-compose up -d
```

### 2. Frontend

```bash
cd project-ck-front-end
pip install -r requirements.txt
streamlit run app.py
```

### 3. Pulseira M5Stack plus 2

```bash
cd project-ck-pulseira-m5stack
cp config.example.py config.py
# Edite config.py com credenciais de WiFi e API
# Faça upload para o dispositivo M5Stack
```

## Documentação

- [Quickstart Frontend](project-ck-front-end/QUICKSTART.md)
- [Integração do Sistema](project-ck-front-end/INTEGRACAO.md)
- [Scripts e Utilitários](project-ck-backend/scripts/README.md)
- [Análise de Dados (CRISP-DM)](docs/data-science/Apresentacao_CRISP-DM.md)

## Funcionalidades

### Para Professores
- Dashboard com visão geral das turmas
- Alertas de crise em tempo real
- Histórico de alertas por aluno
- Gráficos de atividades e sentimentos

### Para Pais
- Acompanhamento do humor diário
- Histórico de atividades
- Comunicação com a escola

### Monitoramento IoT
- Coleta contínua de dados biométricos
- Detecção automática de padrões de crise
- Notificações em tempo real

## Equipe

Projeto desenvolvido como parte do curso de Inteligência Artificial.

## Licença

Este projeto é de uso acadêmico.
