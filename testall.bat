@echo off
cd %~dp0
echo pipenv run python manage.py test --settings config.settings.test %*
pipenv run python manage.py test --settings config.settings.test %*
