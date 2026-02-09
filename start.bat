@echo off
echo 🏠 Iniciando CRM Imobiliário...

REM Check if virtual environment exists
if not exist "venv" (
    echo Criando ambiente virtual...
    python -m venv venv
)

REM Activate virtual environment
echo Ativando ambiente virtual...
call venv\Scripts\activate

REM Install dependencies
echo Instalando dependências...
pip install -r requirements.txt

REM Copy .env if it doesn't exist
if not exist ".env" (
    echo Criando arquivo de configuração...
    copy .env.example .env
)

REM Start the application
echo Iniciando servidor...
cd backend
python app.py
