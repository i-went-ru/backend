#!/bin/bash

# Run Django migrations
python manage.py migrate
python manage.py collectstatic --noinput
# Start Gunicorn server
exec gunicorn -c docker/gunicorn.py back.wsgi:application
