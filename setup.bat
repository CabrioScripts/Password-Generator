@echo off
setlocal

where python >nul 2>&1
if errorlevel 1 (
    echo Python is not installed. Install Python to continue.
    pause
    exit /b 1
)


python -m pip --version >nul 2>&1
if errorlevel 1 (
    echo Pip not found. Installing Pip...
    python -m ensurepip --upgrade
)


echo Installing Modules...
python -m pip install --upgrade colorama
python -m pip install --upgrade pyperclip


echo Done
pause
