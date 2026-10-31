# 🌿 EcoBairro Gestão — PWA de Inventário Off-line (ODS 12)

Sistema de gestão de inventário, controlo de perecibilidade e distribuição de hortifrútis orgânicos para a Associação EcoBairro, alinhado com o Objetivo de Desenvolvimento Sustentável 12 (Consumo e Produção Responsáveis) da ONU.

## 🚀 Arquitetura & Tecnologias
- **Backend:** Python 3.10+ / Flask / Flask-SQLAlchemy / Werkzeug Security
- **Bancos de Dados:** SQLite (Desenvolvimento) / PostgreSQL (Produção)
- **Frontend & PWA:** HTML5, CSS3 (Acessibilidade WCAG AA), JavaScript
- **Segurança:** OWASP Top 10 Compliance (Prevenção contra SQLi, XSS, Broken Auth)

## 📦 Estrutura do Projeto
```text
ecobairro_gestao/
├── app/
│   ├── __init__.py           # Factory Pattern & Configuração do App
│   ├── models.py             # Entidades Produto e MovimentacaoEstoque
│   ├── routes.py             # Controladores das 3 Telas do MVP
│   └── templates/            # Views Jinja2 Acessíveis
├── config.py                 # Gestão de Variáveis de Ambiente
├── requirements.txt          # Dependências do Projeto
└── run.py                    # Entry Point da Aplicação