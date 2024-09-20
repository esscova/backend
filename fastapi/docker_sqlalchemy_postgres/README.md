# FastAPI com Docker e PostgreSQL
Este projeto é uma aplicação FastAPI que utiliza Docker e PostgreSQL para gerenciar usuários. A aplicação permite cadastrar e ler informações de usuários.

## Funcionalidades

- Cadastro de usuários
- Listagem de usuários
- Busca de usuário por ID

## Requisitos

- Docker
- Docker Compose
- Make (opcional, para usar os comandos do Makefile)
## Estrutura
```
.
├── app
│   ├── actions.py
│   ├── database.py
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   └── schemas.py
├── docker-compose.yml
├── Dockerfile
├── Makefile
├── README.md
└── requirements.txt

```
## Como usar

1. Clone o respositório:
```bash
git clone https://github.com/esscova/web-development.git
cd web-development/fastapi/users-docker-postgres/
```

2. Crie e configure um arquivo `.env` na raiz do projeto seguindo o arquivo `.env.example`.

3. Para iniciar a aplicação, execute:

   ```
   make up
   ```

   Ou, se não estiver usando o Makefile:

   ```
   docker-compose -f .docker/docker-compose.yml up -d
   ```

4. A API estará disponível em `http://localhost:8000`

## Endpoints

- `GET /`: Verificar o status da API
- `POST /users/`: Criar um novo usuário
- `GET /users/`: Listar todos os usuários
- `GET /users/{user_id}/`: Buscar um usuário específico por ID

## Comandos úteis (usando Makefile)
- `make help`: Lista todos os comandos configurados no Makefile
- `make up`: Inicia todos os containers
- `make down`: Para e remove todos os containers
- `make restart`: Reinicia todos os containers
- `make logs`: Mostra os logs de todos os serviços
- `make clean`: Remove arquivos temporários e containers parados
- `make rebuild`: Reconstrói e reinicia os containers Docker

## Desenvolvimento

Para desenvolver e testar localmente:

1. Instale as dependências:

   ```
   pip install -r requirements.txt
   ```

2. Execute o servidor de desenvolvimento:

   ```
   uvicorn app.main:app --reload
   ```


## Contribuindo

Sinta-se à vontade para abrir issues ou pull requests para melhorar este projeto.