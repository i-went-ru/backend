# pull official base image
FROM python:3.11.4-slim-buster

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .

EXPOSE 8000
#нужно для админки
#TODO нужна ли админка?
#RUN python manage.py collectstatic --noinput

ENTRYPOINT ["python","manage.py", "migrate"]
CMD ["gunicorn", "-c", "docker/gunicorn.py", "iwent-backend.wsgi:application"]