#!/usr/bin/env bash
python manage.py makemigrations
python manage.py migrate
python manage.py seed_db --create-super-user

python manage.py runserver ${DJANGO_BIND_ADDRESS}:${DJANGO_BIND_PORT}
