# Livros

Servidor simples desenvolvido pelo aluno Vinícius G. Mendonça para disciplina de DevOps da 
Especialização em Engenharia de Serviços e Sistemas de Cloud Computing, turma de 2026.

## Executando o servidor

Se você estiver usando no devcontainer, todas as dependências já estarão instaladas e prontas para uso.
Basta executar na linha de comando:

```bash
flask --app server run --debug
```

Os testes unitários também podem ser executados través do pytest:
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