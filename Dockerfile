# pull official base image
FROM python:3.8.0-alpine

# set work directory
RUN mkdir /rest-api-service
RUN mkdir /rest-api-service/staticfiles
WORKDIR /rest-api-service

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /rest-api-service/requirements.txt
RUN pip install -r requirements.txt

# copy wait script and project
COPY ./wait_to_start.sh /rest-api-service/wait_to_start.sh
COPY . /rest-api-service

EXPOSE 8000

#CMD gunicorn -b :8000 nerfapi.wsgi
ENTRYPOINT ["/rest-api-service/wait_to_start.sh"]
