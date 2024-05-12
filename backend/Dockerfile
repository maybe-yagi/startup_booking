FROM python:3.11.9-alpine3.19

WORKDIR /usr/src/app/backend
ENV FLASK_APP=api
ENV FLASK_ENV=development

COPY /requirements.txt ./

RUN pip install --upgrade pip
RUN pip install -r requirements.txt