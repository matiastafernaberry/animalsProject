FROM django
WORKDIR /usr/src/app
CMD [ "django-admin", "startproject pythonChallenge" ]
CMD [ "python", "manage.py runserver 0.0.0.0:8000" ]