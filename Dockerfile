# Base image
FROM python:3.8.13-slim-buster

# Dependency for psycopg3
RUN apt-get update -y && apt-get upgrade -y
RUN apt-get install -y libgdal-dev build-essential libpq-dev

# Environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Working directory
WORKDIR /onyesha

# Installing requirements
COPY requirements.txt /onyesha/

RUN pip install -r requirements.txt


# Copy project files and directories
COPY . /onyesha/