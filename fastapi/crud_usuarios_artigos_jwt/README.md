# FastAPI com SQLAlchemy, SQLite assíncrono e Autenticação JWT

## Descrição
Este projeto implementa uma API utilizando **FastAPI** para gerenciamento de artigos e usuários. O sistema permite operações de CRUD para os modelos de `artigo` e `usuario`, com autenticação e segurança integradas.

## Estrutura do Projeto

- **main.py**: Arquivo principal que inicia o servidor FastAPI.
- **criar_tabelas.py**: Script para criação das tabelas no banco de dados.
- **api/v1/**:
  - **api.py**: Arquivo que organiza as rotas da versão 1 da API.
  - **endpoints/**:
    - **artigo.py**: Endpoints relacionados ao gerenciamento de artigos.
    - **usuario.py**: Endpoints relacionados ao gerenciamento de usuários.
- **core/**:
  - **configs.py**: Configurações gerais do projeto.
  - **database.py**: Configuração e conexão com o banco de dados.
  - **deps.py**: Dependências utilizadas nos endpoints.
  - **security.py**: Implementação de segurança e autenticação.
  - **auth.py**: Funções relacionadas à autenticação de usuários.
- **models/**:
  - **artigo_model.py**: Definição do modelo de dados para artigos.
  - **usuario_model.py**: Definição do modelo de dados para usuários.
  - **__all_models.py**: Importa e registra todos os modelos.
- **schemas/**:
  - **artigo_schema.py**: Esquema de validação de dados para artigos.
  - **usuario_schema.py**: Esquema de validação de dados para usuários.

## Como executar o projeto

1. Clone o repositório:
   ```bash
   git clone https://github.com/esscova/web.git
   cd web/fastapi/crud_usuarios_artigos_jwt
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Execute o script para criar as tabelas no banco de dados:
   ```bash
   python criar_tabelas.py
   ```

4. Inicie o servidor FastAPI:
   ```bash
   python main.py
   ```

5. Acesse a documentação da API:
   - Documentação Swagger: `http://127.0.0.1:8000/docs`
   - Documentação Redoc: `http://127.0.0.1:8000/redoc`

## Funcionalidades

- Gerenciamento de artigos (criação, leitura, atualização e exclusão).
- Gerenciamento de usuários (criação, leitura, atualização e exclusão).
- Autenticação JWT para proteger rotas.
