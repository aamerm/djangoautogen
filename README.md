# djangoautogen
using django-baker plugin

- django-admin startproject djangoautogen
- python3 manage.py startapp fas
- add models in models.py
- https://github.com/krisfields/django-baker
- python3 manage.py makemigrations fas
- python3 manage.py migrate fas
- python3 manage.py runserver 8080

postgresql
- createuser fas
- createdb fasdb -O fas
- add those details in settings.py along with proper engine name
