# Livros

Servidor simples desenvolvido pelo aluno Vinícius G. Mendonça para disciplina de DevOps da 
Especialização em Engenharia de Serviços e Sistemas de Cloud Computing, turma de 2026.

<img width="996" height="708" alt="image" src="https://github.com/user-attachments/assets/8a4f6b10-f6a6-41d0-930f-93e8735fc772" />

## Endpoints da API

A API implementa dois endpoints principais:

- `GET /api/livros`: Inserção de um livro
- `POST /api/livros`: Listagem de livros

A home (`GET /`) do servidor fornece uma landing page com o link para documentação swagger.

## Executando o servidor

Se você estiver usando no devcontainer, todas as dependências já estarão instaladas e prontas para uso.
Basta executar na linha de comando:

```bash
flask --app server run --debug
```

Os testes unitários também podem ser executados através do pytest:
```bash
pytest -v
```

Por fim, há um linter para rastrear possíveis bugs e má práticas de código:
```bash
ruff check --fix
ruff format
```

## Instalando as dependências

Para executar da sua máquina, instale o Python 3.14 e execute os seguintes comandos:

1. Instale o [Python 3.14](https://www.python.org/downloads/)
2. Crie o ambiente virtual do projeto
```bash
python -m venv .venv
```

3. Inicie o ambiente:

No Windows:
```bash
.venv\\Scripts\\activate
```

No Linux ou macOS:
```bash
source .venv/bin/activate
```

4. Instale as dependências do arquivo requirements.txt

```bash
pip install -r requirements.txt
pip install -e .
```
