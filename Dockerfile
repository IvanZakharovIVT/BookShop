FROM python:3.12-alpine

WORKDIR /app

RUN apk update && apk add --no-cache python3 py3-setuptools py3-pip

COPY Pipfile Pipfile.lock ./
RUN pip install pipenv
RUN pipenv install --system --deploy

COPY . /app
