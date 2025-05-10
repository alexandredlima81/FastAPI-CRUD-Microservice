# FastAPI CRUD Microservice

Este projeto é um exemplo de microserviço RESTful construído com **FastAPI**, implementando um CRUD completo (Create, Read, Update, Delete) com armazenamento em memória.

---

## Tecnologias Utilizadas

- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/)
- Python 3.8+

---

## Como Executar

### 1. Clonar o repositório

```bash
git clone https://github.com/seuusuario/fastapi-crud.git
cd fastapi-crud
```
### 2. Criar um ambiente virtual (opcional, mas recomendado)

``` bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```
### 3. Instalar as dependências

```bash
pip install fastapi uvicorn
```
### 4. Rodar a aplicação

```bash
uvicorn main:app --reload
```
### 5. Acessar a API

Documentação interativa (Swagger): http://localhost:8000/docs

Documentação alternativa (ReDoc): http://localhost:8000/redoc

## Estrutura do Projeto

```bash
fastapi-crud/
├── main.py         # Aplicação FastAPI com as rotas CRUD
├── models.py       # Modelo de dados Pydantic
└── README.md       # Documentação do projeto
```
## Funcionalidades

GET /items - Lista todos os itens

GET /items/{id} - Obtém item específico

POST /items - Cria um novo item

PUT /items/{id} - Atualiza item existente

DELETE /items/{id} - Remove item

## Observações

Os dados são armazenados em memória, ou seja, são perdidos quando o servidor é reiniciado.

Para persistência real, pode-se integrar com um banco como SQLite, PostgreSQL etc.

## Licença
Este projeto está sob a licença MIT
