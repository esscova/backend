# Currency Converter API

Este projeto é uma API de conversão de moedas construída com FastAPI. Ela consome a API [Alpha Vantage](https://www.alphavantage.co/#page-top) para obter taxas de câmbio em tempo real e oferece endpoints para converter valores entre diferentes moedas.

## Funcionalidades

- Conversão síncrona de moedas
- Conversão assíncrona de moedas
- Suporte para conversão entre múltiplas moedas simultaneamente

## Estrutura do Projeto

```
.
├── main.py
├── routers.py
├── converter.py
└── models.py
```

- `main.py`: Ponto de entrada da aplicação FastAPI
- `routers.py`: Define as rotas e endpoints da API
- `converter.py`: Contém a lógica de conversão de moedas
- `models.py`: Define os modelos Pydantic para validação de entrada e saída

## Endpoints

1. `/converter/{from_currency}`: Conversão síncrona
2. `/converter/async/{from_currency}`: Conversão assíncrona
3. `/converter/async/v2/{from_currency}`: Conversão assíncrona com modelo de entrada

## Configuração

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/esscova/web.git
   cd web/fastapi/currency_converter
   ```

2. **Crie e ative um ambiente virtual:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

3. **Instale as dependências:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Execute:**

   ```bash
   uvicorn main:app --reload
   ```

5. **Configure as variáveis de ambiente:**
   - `API_KEY`: Sua chave da API Alpha Vantage para requisições.


## Como executar

Para iniciar o servidor:

```bash
uvicorn main:app --reload
```

Acesse a documentação interativa da API em `http://localhost:8000/docs`

## Exemplos de Uso

### Conversão Síncrona

```
GET /converter/USD?to_currencies=BRL,EUR&price=100
```

### Conversão Assíncrona

```
GET /converter/async/USD?to_currencies=BRL,EUR,JPY&price=100
```

### Conversão Assíncrona v2

```
GET /converter/async/v2/USD

Body:
{
  "price": 100,
  "to_currencies": ["BRL", "EUR", "JPY"]
}
```

## Notas

- Este projeto utiliza a API Alpha Vantage para obter taxas de câmbio em tempo real. Certifique-se de respeitar os limites de requisições da sua chave de API.
- A validação de entrada é implementada usando Pydantic e parâmetros de caminho/consulta do FastAPI.

## Contribuições

Contribuições são bem-vindas! Por favor, abra uma issue para discutir mudanças propostas ou envie um pull request.

