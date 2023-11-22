#!/bin/bash

# Run Django migrations
python manage.py migrate

# Start Gunicorn server
exec gunicorn -c docker/gunicorn.py back.wsgi:application
