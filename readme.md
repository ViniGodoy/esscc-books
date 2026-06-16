# Livros

Servidor simples desenvolvido pelo aluno Vinícius G. Mendonça para disciplina de DevOps da 
Especialização em Engenharia de Serviços e Sistemas de Cloud Computing, turma de 2026.

## Instalando as dependências

Se você estiver usando no devcontainer, o container já é gerado com todas as dependências instaladas. 
Pule diretamente para o passo [Executando o servidor](#Executando-o-servidor).

```bash
python -m venv .venv
```

3. Inicie-o()

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
```

## Executando o servidor

Pela linha de comando, rode:

```bash
flask --app books run --debug
```

## Ambiente e dependências

Feito para **Python 3.14**

Bibliotecas:
* Flask 3.1.x
* Flask SQL Alchemy 3.1.x
* SQL Alchemy 2.0.x
* Pytest 9.1.x