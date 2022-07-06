# Base image
FROM python:3.8.13-slim-buster

# Environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Working directory
WORKDIR /onyesha

# Installing requirements
COPY requirements.txt requirements.txt /onyesha/

RUN pip install -r requirements.txt


# Copy project files and directories
COPY . /onyesha/