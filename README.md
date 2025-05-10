# FastAPI CRUD Microservice com PostgreSQL e Docker

Este projeto é um exemplo de microserviço RESTful construído com **FastAPI**, implementando um CRUD completo (Create, Read, Update, Delete) com persistência de dados em **PostgreSQL**, empacotado com **Docker**.

---

## Tecnologias Utilizadas

- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/)
- [PostgreSQL](https://www.postgresql.org/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Docker](https://www.docker.com/)
- [Pytest](https://docs.pytest.org/)

---

## Como Executar o Projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/alexandredlima81/FastAPI-CRUD-Microservice.git
cd FastAPI-CRUD-Microservice
```
### 2. Subir com Docker Compose
```bash
docker-compose up --build
```
### 3. Acessar a API
Swagger: http://localhost:8000/docs

ReDoc: http://localhost:8000/redoc

🧪 Executando Testes Automatizados
```bash
docker run --rm -v $PWD:/app -w /app python:3.11 bash -c "pip install -r requirements.txt && pytest"
```
📁 Estrutura do Projeto
```bash

FastAPI-CRUD-Microservice/
├── app/
│   ├── __init__.py
│   ├── main.py          # Ponto de entrada da aplicação FastAPI
│   ├── models.py        # Modelos SQLAlchemy
│   ├── schemas.py       # Schemas Pydantic
│   └── crud.py          # Operações CRUD
├── test_main.py         # Testes automatizados com pytest
├── requirements.txt     # Dependências do projeto
├── Dockerfile           # Dockerfile da aplicação FastAPI
├── docker-compose.yml   # Orquestração com PostgreSQL
└── README.md            # Este arquivo
```
## Endpoints

GET /items — Lista todos os itens

GET /items/{id} — Retorna um item específico

POST /items — Cria um novo item

PUT /items/{id} — Atualiza um item existente

DELETE /items/{id} — Deleta um item existente

## Observações
Os dados são persistidos em um banco PostgreSQL.

Recomendado para projetos que buscam escalabilidade com APIs modernas.

Fácil integração com sistemas de autenticação, mensageria, cache, etc.

## Licença
Este projeto está licenciado sob os termos da licença MIT.
