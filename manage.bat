@echo off
cd %~dp0
echo pipenv run python manage.py %*
pipenv run python manage.py %*
