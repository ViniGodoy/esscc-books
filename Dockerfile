# Usa uma imagem base mais leve e específica
FROM python:3.14-slim

# Define o diretório de trabalho
WORKDIR /app

# Melhora o cache do Docker copiando primeiro o requirements.txt
COPY requirements.txt .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia o código da aplicação para o contêiner
COPY . .

# Instala o projeto para que o flask o encontre
RUN pip install .

# Define a variável de ambiente para o Flask
ENV FLASK_APP=server

# Expõe a porta que o Flask usa
EXPOSE 5000

# O comando de inicialização aplica as migrações e depois inicia o servidor.
# Isso garante que o banco de dados esteja sempre atualizado quando o contêenter sobe.
CMD ["bash", "-c", "flask db upgrade && flask run --host=0.0.0.0"]
