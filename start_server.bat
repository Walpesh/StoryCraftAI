@echo off
echo Остановка nginx (если он запущен)...
taskkill /F /IM nginx.exe >nul 2>&1

echo Запуск nginx...
start "" "C:\VScode\bookgen\nginx-1.27.5\nginx.exe"

echo Активация виртуального окружения...
call C:\VScode\bookgen\venv\Scripts\activate.bat 

echo Запуск uvicorn на 0.0.0.0:8000...
call uvicorn main:app --host 0.0.0.0 --port 8000

pause