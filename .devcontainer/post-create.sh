#!/bin/bash

# Para o script se houver erros
set -e

# Adiciona a variável de ambiente ao perfil do shell para futuras sessões
echo 'export FLASK_APP=server' >> ~/.bashrc
# Exporta a variável para a sessão atual
export FLASK_APP=server

echo "--- Instalando dependências Python ---"
pip3 install --user -r requirements.txt
pip3 install -e .

echo "--- Configurando as migrações do banco de dados ---"

# Inicializa o diretório de migrações, somente se ele não existir
if [ ! -d "migrations" ]; then
    echo "Diretório de migrações não encontrado. Executando 'flask db init'..."
    flask db init
else
    echo "Diretório de migrações já existe."
fi

# Gera um script de migração. O '|| true' evita que o script falhe se não houver mudanças.
echo "Gerando script de migração inicial..."
flask db migrate -m "Configuração inicial do banco de dados" || true

# Aplica a migração ao banco de dados
echo "Aplicando migrações ao banco de dados..."
flask db upgrade

echo "--- Ambiente de desenvolvimento configurado com sucesso! ---"
