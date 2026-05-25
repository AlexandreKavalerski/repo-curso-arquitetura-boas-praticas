# code-curso-fundamentos-arquitetura

## Requisitos

- [uv](https://docs.astral.sh/uv/#installation) para gerenciamento de dependências e ambiente virtual.

## Como rodar o projeto

1. Instale as dependências:

   ```bash
   uv sync
   ```

2. Ative o ambiente virtual:

   ```bash
   source .venv/bin/activate
   ```

3. Popule o banco de dados com dados iniciais (Seed):

   ```bash
   uv run seed.py
   ```

4. Inicie o servidor:

   ```bash
   uv run fastapi dev app/main.py
   ```
