#!/bin/sh

docker-compose exec rest-api python manage.py makemigrations --noinput
docker-compose exec rest-api python manage.py migrate --noinput

