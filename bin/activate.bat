@echo off

REM Activate Pipenv environment
echo Activating Pipenv environment...
pipenv shell

REM Install packages from requirements.txt
echo Installing packages from requirements.txt...
pipenv install -r ../requirements.txt

echo Script completed.