FROM python:3.9

COPY requirements.txt /temp/requirements.txt
WORKDIR /WebApp
EXPOSE 8000


RUN pip install -r /temp/requirements.txt

RUN adduser --disabled-password service-user

USER service-user
