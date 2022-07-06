# Base image
FROM python:3.8.13-slim-buster

# Install dependencies
RUN apt-get update -y && apt-get upgrade -y

RUN apt-get install -y libgdal-dev libpq-dev

# Environment variables
ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

# Working directory

WORKDIR /onyesha

# Installing dependencies

COPY requirements.txt requirements.txt /onyesha/

RUN pip install --upgrade --no-cache-dir -r requirements.txt


# Copy project files and directories

COPY . /onyesha/