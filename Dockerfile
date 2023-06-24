# Base image
FROM python:3.10.12-slim-buster

# install dependencies for psycopg3
RUN apt-get update -y && apt-get upgrade -y
RUN apt-get install -y libgdal-dev build-essential libpq-dev

# environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# create directory for the app user
RUN mkdir -p /home/geouser

# don't run as root therefore create non-root user
RUN groupadd --gid 1001 geouser && \
    useradd --uid 1001 --gid geouser --home /home/geouser geouser

# install pipenv
RUN pip install pipenv

# create user, project and static files directories
ENV HOME=/home/geouser
ENV APP_HOME=/home/geouser/nairobi_busstops
RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/staticfiles
RUN mkdir $APP_HOME/mediafiles
WORKDIR $APP_HOME

# Copy pipenv files
COPY Pipfile Pipfile.lock $APP_HOME
# Install development packages
RUN pipenv install --system

# copy project files and sub-directories
COPY . $APP_HOME

# change ownership of working directory
RUN chown -R geouser:geouser $APP_HOME

# change to the app user
USER geouser

