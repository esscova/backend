# FastAPI com SQLAlchemy e SQLite

Este projeto é uma API desenvolvida com **FastAPI**, **SQLAlchemy** (assíncrono) e **SQLite** para gerenciar cursos. Ele permite criar, listar, visualizar, atualizar e deletar cursos em um banco de dados.

## Tecnologias Utilizadas

- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy (Assíncrono)](https://docs.sqlalchemy.org/en/14/orm/extensions/asyncio.html)
- [SQLite com aiosqlite](https://docs.sqlalchemy.org/en/14/dialects/sqlite.html#using-aiosqlite)
- [Pydantic](https://docs.pydantic.dev/)
- [Uvicorn](https://www.uvicorn.org/)

## Requisitos

- **Python 3.9+**
- **Virtualenv** (recomendado)

## Instalação e Configuração

1. Clone o repositório:

```bash
git clone https://github.com/esscova/web.git
cd web/fastapi/crud-sqlalchemy-sqlite/
```

2. Crie e ative um ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate  # Linux/MacOS
venv\Scripts\activate      # Windows
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Crie o arquivo de banco de dados e as tabelas executando o script `criar_tabelas.py`:

```bash
python criar_tabelas.py
```

5. Inicie o servidor:

```bash
python main.py
```

O servidor estará rodando em [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Estrutura do Projeto

```
.
├── api
│   └── v1
│       ├── api.py
│       └── endpoints
│           └── cursos.py
├── core
│   ├── configs.py
│   ├── database.py
│   └── deps.py
├── models
│   ├── __all_models.py
│   └── curso_model.py
├── schemas
│   └── curso_schema.py
├── create_tables.py
├── main.py
└── requirements.txt
```

- **`api/v1/endpoints/cursos.py`**: Contém os endpoints CRUD para o recurso "curso".
- **`core/configs.py`**: Configurações da aplicação, como o caminho do banco de dados.
- **`core/database.py`**: Configuração da sessão do banco de dados assíncrono.
- **`models/curso_model.py`**: Modelo do curso utilizado pelo SQLAlchemy.
- **`schemas/curso_schema.py`**: Esquema de validação do curso usando Pydantic.
- **`criar_tabelas.py`**: Script para criar as tabelas no banco de dados.
- **`main.py`**: Arquivo principal que inicia a aplicação FastAPI.

## Endpoints

- **POST** `/api/v1/cursos/`: Cria um novo curso.
- **GET** `/api/v1/cursos/`: Retorna todos os cursos.
- **GET** `/api/v1/cursos/{curso_id}`: Retorna um curso específico.
- **PUT** `/api/v1/cursos/{curso_id}`: Atualiza um curso específico.
- **DELETE** `/api/v1/cursos/{curso_id}`: Deleta um curso específico.

## Exemplo de Requisição
A documentação estará rodando em [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).
### Criar um Curso

```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/api/v1/cursos/' \
  -H 'Content-Type: application/json' \
  -d '{
  "titulo": "Curso de FastAPI",
  "aulas": 10,
  "horas": 20
}'
```

### Listar todos os cursos

```bash
curl -X 'GET' 'http://127.0.0.1:8000/api/v1/cursos/'
```

## Contribuindo

1. Faça um fork do projeto.
2. Crie uma nova branch (`git checkout -b feature/nova-funcionalidade`).
3. Commit suas mudanças (`git commit -am 'Adiciona nova funcionalidade'`).
4. Envie para a branch original (`git push origin feature/nova-funcionalidade`).
5. Crie um Pull Request.

