@echo off
title Assistente de Risco Academico

cd /d "%~dp0"

echo ==========================================
echo   ASSISTENTE DE RISCO ACADEMICO
echo ==========================================
echo.
echo Iniciando o aplicativo...
echo.

if not exist "venv\Scripts\python.exe" (
    echo ERRO: O ambiente virtual nao foi encontrado.
    echo.
    echo Execute primeiro:
    echo python -m venv venv
    echo python -m pip install -r requirements.txt
    echo.
    pause
    exit /b 1
)

"venv\Scripts\python.exe" -m streamlit run "src\app.py"

echo.
echo O aplicativo foi encerrado.
pause