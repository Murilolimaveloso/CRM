#!/bin/bash

echo "🏠 Iniciando CRM Imobiliário..."

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Criando ambiente virtual..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "Ativando ambiente virtual..."
source venv/bin/activate

# Install dependencies
echo "Instalando dependências..."
pip install -r requirements.txt

# Copy .env if it doesn't exist
if [ ! -f ".env" ]; then
    echo "Criando arquivo de configuração..."
    cp .env.example .env
fi

# Start the application
echo "Iniciando servidor..."
cd backend
python app.py
