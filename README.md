# Pet Adoption Project

This project uses django and django-rest framework. It provides admin interface, a json API, and use google authentication for user login.

## How to run it

 * virtualenv env
 * source env/bin/active
 * export SECRET_KEY='xxx'
 * export SOCIAL_AUTH_GOOGLE_OAUTH2_KEY='xxx'
 * export SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET='xxx'
 * python manage.py makemigrations adoption
 * python manage.py migrate
 * python manage.py createsuperuser
 * python manage.py runserver

You can put your environment variables in a file called export.sh which will be ignored by git
