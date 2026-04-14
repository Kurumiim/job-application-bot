# Job Application Bot

Bot para análise de vagas, comparação com currículo, geração de score de compatibilidade e preenchimento automático de formulários com revisão humana antes do envio final.

## Stack inicial
- Python
- FastAPI
- Playwright
- PostgreSQL
- Redis
- Docker

## Como rodar localmente

1. Ativar o ambiente virtual:
   source .venv/bin/activate

2. Subir serviços:
   docker-compose up -d

3. Rodar a API:
   uvicorn app.main:app --reload

4. Testar:
   curl http://localhost:8000
