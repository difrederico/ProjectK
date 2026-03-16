# 📁 Scripts do Project-CK Backend

Scripts utilitários para manutenção, testes e demonstrações do sistema.

##  Estrutura

```
scripts/
├── demos/          # Scripts de demonstração e apresentação
├── seeds/          # Scripts para popular o banco de dados
├── utils/          # Utilitários gerais
└── README.md
```

---

## Demos (`/demos/`)

Scripts para demonstrações e apresentações do sistema.

| Script | Descrição | Uso |
|--------|-----------|-----|
| `demo_alertas_apresentacao.py` | Menu interativo para gerar alertas de crise | `python scripts/demos/demo_alertas_apresentacao.py` |
| `gerar_alerta_simples.py` | Gera um alerta simples rapidamente | `python scripts/demos/gerar_alerta_simples.py` |
| `teste_pipeline_pulseira.py` | Testa o pipeline completo IoT (MQTT→Redis→MongoDB) | `python scripts/demos/           teste_pipeline_pulseira.py` |

---

##  Seeds (`/seeds/`)

Scripts para popular o banco de dados com dados iniciais ou de teste.

| Script | Descrição | Uso |
|--------|-----------|-----|
| `popular_dados_teste.py` | Popula banco com usuários, turmas e alunos de teste | `python scripts/seeds/popular_dados_teste.py` |
| `populate_feelings.py` | Adiciona registros de sentimentos dos alunos | `python scripts/seeds/populate_feelings.py` |
| `populate_mongo.py` | Seed geral do MongoDB | `python scripts/seeds/populate_mongo.py` |

---

## 🔧 Utils (`/utils/`)

Utilitários para manutenção e operações do sistema.

| Script | Descrição | Uso |
|--------|-----------|-----|
| `train_model.py` | Treina/re-treina o modelo de ML | `python scripts/utils/train_model.py` |
| `iot_simulator.py` | Simula dados IoT de pulseiras | `python scripts/utils/iot_simulator.py` |
| `export_db.py` | Exporta dados do MongoDB para CSV | `python scripts/utils/export_db.py` |
| `simulate_activity.py` | Simula atividades de alunos | `python scripts/utils/simulate_activity.py` |

---

##  Observações

1. **Execute da raiz do backend:**
   ```bash
   cd project-ck-backend
   python scripts/demos/demo_alertas_apresentacao.py
   ```

2. **Docker deve estar rodando** para scripts que acessam MongoDB/Redis/MQTT

3. **Variáveis de ambiente** devem estar configuradas no `.env`
