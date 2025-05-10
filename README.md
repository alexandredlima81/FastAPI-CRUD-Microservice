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

## Pré-requisitos

- Docker 20.10+

- Docker Compose 1.29+

- Python 3.11 (opcional para desenvolvimento local)

---

## Estrutura do Projeto
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

---

## Como Executar o Projeto

### 1. Com Docker (recomendado)

```bash
# Clonar repositório
git clone https://github.com/alexandredlima81/FastAPI-CRUD-Microservice.git
cd FastAPI-CRUD-Microservice
```
```bash
# Iniciar containers
docker-compose up --build
```
- Acessar a API:

Swagger: http://localhost:8000/docs

ReDoc: http://localhost:8000/redoc

```bash
# Finalizar containers
docker-compose down -v
```

### 2. Sem Docker (desenvolvimento)

python -m venv venv
source venv/bin/activate  # Linux/MacOS
venv\Scripts\activate     # Windows

pip install -r requirements.txt
uvicorn app.main:app --reload

## 3. Executando Testes Automatizados

Para executar os testes:

```bash
# Com Docker
docker-compose exec web pytest
```
```bash
# Localmente (com venv ativado)
pytest
```

## 34. Os teste de todos os endpoints, podem ser realizados diretamente na documentação interativa:

Swagger: http://localhost:8000/docs

ReDoc: http://localhost:8000/redoc

---

## Endpoints da API

|Método	| Endpoint	    | Descrição                         | Schema de Entrada	| Status Code de Sucesso | Schema de Resposta
| ----- | ------------- | --------------------------------- | ----------------- | ---------------------- | ------------------- |
|POST	| `/items/`   	| Cria um novo item	ItemCreate	    | `ItemCreate`      | 201 (Created)	         | `Item`              |
|GET	| `/items/`     | Lista todos os itens (paginação)	| -	                | 200 (OK)	             | `List[Item]`        |
|GET	| `/items/{id}`	| Obtém um item específico	    	| -	                | 200 (OK)	             | `Item`              |
|PUT	| `/items/{id}`	| Atualiza um item existente	    | `ItemUpdate`    	| 200 (OK)	             | `Item`              |
|DELETE	| `/items/{id}`	| Remove um item	                | -	                | 200 (OK)	             | `DeleteResponse`    |

---

## Detalhes dos Schemas:

### ItemCreate:

```json
{
  "title": "string",
  "description": "string (opcional)"
}
```
### ItemUpdate:

```json
{
  "title": "string (opcional)",
  "description": "string (opcional)"
}
```
### Item (Resposta):

```json
{
  "id": "integer",
  "title": "string",
  "description": "string (opcional)"
}
```
### DeleteResponse:

```json
{
  "status": "string",
  "message": "string",
  "id": "integer"
}
```
---

## Parâmetros de Query (GET /items/):

- skip: Número de itens para pular (default: 0)

- limit: Limite de itens por página (default: 100)
---
## Exemplo de requisição:

```bash
GET /items/?skip=0&limit=10
```
---
## Códigos de Erro Comuns:
- 400 Bad Request: Validação falhou

- 404 Not Found: Item não encontrado

- 500 Internal Server Error: Erro no servidor

---

## Documentação da API

A API oferece dois formatos de documentação interativa:

Swagger UI: http://localhost:8000/docs

ReDoc: http://localhost:8000/redoc

---

## Persistência de Dados
PostgreSQL 13 como banco de dados principal

SQLAlchemy 2.0 como ORM

Dados persistidos em volume Docker (postgres_data)
## Recursos Avançados
Validação de dados com Pydantic v2

Tratamento de erros global

Paginação automática

Documentação OpenAPI automática

Health Check endpoint (/db-health)
## Variáveis de Ambiente
O projeto utiliza as seguintes variáveis (configuradas no docker-compose.yml):

DATABASE_URL: URL de conexão com o PostgreSQL

POSTGRES_USER: Usuário do banco de dados

POSTGRES_PASSWORD: Senha do banco de dados

POSTGRES_DB: Nome do banco de dados

## Licença
Este projeto está licenciado sob os termos da licença MIT.

## Recursos Futuros
Autenticação JWT

Sistema de cache com Redis

Monitoramento com Prometheus

Logs estruturados

Migrações de banco com Alembic