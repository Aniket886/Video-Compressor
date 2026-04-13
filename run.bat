@echo off
chcp 65001 > nul
echo ==========================================
echo    CompressVideo - Desktop App
echo ==========================================
echo.

:: Check if Python is installed
python --version > nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.7 or later from https://python.org
    pause
    exit /b 1
)

echo Starting CompressVideo...
python main.py

if errorlevel 1 (
    echo.
    echo App exited with an error.
    pause
)
