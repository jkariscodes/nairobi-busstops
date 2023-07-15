# Nairobi Bus Stops WebMap

---

![nairobi-bus-stops](https://github.com/jkariscodes/nairobi-busstops/assets/23359514/56a667f0-6904-4d6c-812d-e324e3a83f28)

---
A simple Web GIS application developed in Django, Django REST framework, and Leaflet. This app renders bus stops from the database and parses them into a leaflet map.

## Table of Contents
  - [Description](#description)
  - [Features](#features)
  - [Software](#software)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Tests](#tests)
  - [License](#license)
  - [Questions](#questions)
  - [References](#references)

## Description
This is a simple web geographic information systems (GIS) application that demonstrates full-stack GIS web development using Django, Django REST framework, JavaScript, CSS and HTML and one that can be forked and customized to your preference.

# Requirements
1. Python - https://www.python.org/downloads/
2. PostgreSQL - https://www.postgresql.org/download/
3. PostGIS - https://postgis.net/install/ 
4. Docker (optional but fast to deploy). - https://docs.docker.com/get-docker/ 

## Features

Features present in this project include:

1. Responsive and mobile-friendly user interface.
2. Map location markers with event-driven capabilities.
3. Static files (css, javascript, and images) management.
4. Development and production environment configurations.
5. Containerized deployment configuration.
6. Code formatting / linting support.
7. Unit testing (To be done).

## Software

### Software and Tools

Software used in the development of this project include:
  - **[Python](https://www.python.org/downloads/release/python-31012/)** - Core programming language used in the development of this project. Specific version is referenced in the [development](Dockerfile-dev) and [production](Dockerfile) build configurations.
  - **[Django](https://docs.djangoproject.com/en/4.2/topics/install/)** - Python web development framework that is the main framework used in this project.
  - **[Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)** - Used for version control in development of this project.
  - **[Docker Desktop Windows](https://docs.docker.com/desktop/windows/install/)** - Software for handling development operations (DevOps) using graphical user interface (GUI) in Windows. Installs Docker Command Line Interface, Docker Compose etc.
  - **[Docker Desktop Linux](https://docs.docker.com/desktop/linux/install/)** - Software for handling development operations (DevOps) using graphical user interface (GUI) in Linux.
  - **[Postgres](https://hub.docker.com/_/postgres?tab=tags)** - Object Relational Database Management System used to store and support DB operations in this project. Specific version is referenced in [development](docker-compose-dev.yml) and [production](docker-compose-dev.yml) configurations.

### Dependencies

This project's initial dependencies are listed in the [Pipfile](Pipfile) include: 
* [__Django__](https://docs.djangoproject.com/) as the base framework
* [__django-rest-framework__](https://www.django-rest-framework.org) for REST api functionalities.
* [__django-rest-framework-gis__](https://github.com/openwisp/django-rest-framework-gis) To provide Geographic add-ons for Django REST Framework.
* [__django-environ__](https://django-environ.readthedocs.org/) for management of environment variables
* [__django-geojson__](https://django-geojson.readthedocs.io/) for manipulating GeoJSON with Django
* [__django-leaflet__](https://django-leaflet.readthedocs.io/en/latest/) for adding leaflet functionality and assets to Django/GeoDjango
* [__django-storages__](https://github.com/jschneier/django-storages) support for Amazon's S3 storage backend. Can be used with other storage backends e.g. Digital Ocean, DropBox, Google Cloud etc. 
* [__django-cloudinary-storage__](https://github.com/klis87/django-cloudinary-storage) Package that facilitates integration with Cloudinary using [Django File Storage API](https://docs.djangoproject.com/en/4.1/ref/files/storage/)on the management of media and static files. Read more from [Cloudinary documentation](https://cloudinary.com/documentation/django_integration)
* [__psycopg-binary__](https://www.psycopg.org/docs/) database adapter to facilitate database connectivity and other operations.
* [__django-cors-headers__](https://github.com/adamchainz/django-cors-headers) Applied in handling the server headers required for Cross-Origin Resource Sharing (CORS).
* [__Django Debug Toolbar__](https://django-debug-toolbar.readthedocs.io/) to help with debugging during development
* [__whitenoise__](https://github.com/evansd/whitenoise) for managing static and user uploads in developement and production
* [__gunicorn__](https://gunicorn.org/) HTTP server for supporting serving of this project over the web
* [__dj-database-url__](https://github.com/jazzband/dj-database-url) support for database URL environment variable
* [__boto3__](https://github.com/boto/boto3) supporting Amazon's S3 capabilities
* [__black__](https://github.com/psf/black) for linting and automatically formatting the code during development
* [__Faker__](https://faker.readthedocs.io) for generating fake data for use/test in this project (TODO)
* [__coverage__](https://coverage.readthedocs.io/) for measuring code coverage (TODO)

## Installation
The minimum requirement required to deploy this project is [Docker Engine](). Docker Engine contains docker, [docker compose](), and if on a Desktop environment and prefer a graphical user interface, one can make use of [Docker Desktop]().

[Make](https://www.gnu.org/software/make/manual/make.html) is used in this project to execute docker commands present in the [Makefile](Makefile) for the purpose of saving time that is used during executing long docker commands. This is optional but __recommended__ and can be installed using the following guides
- [Installation on Linux](https://linuxhandbook.com/using-make/)
- Installing Make on Windows requires a bit of setup since Make is not natively available on the platform. Here are the steps to follow:

   -  Download and install the [Windows Subsystem for Linux](https://learn.microsoft.com/en-us/windows/wsl/install) (WSL) from the Microsoft Store. This will allow you to run a Linux environment on your Windows machine.

    - Once WSL is installed, open the Microsoft Store and search for a Linux distribution that includes make, such as [Ubuntu](https://apps.microsoft.com/store/detail/ubuntu-on-windows/9NBLGGH4MSV6). Download and install the distribution.

    - Open the Linux distribution from the Start menu or by typing the name of the distribution in the search bar.

    - In the Linux terminal, type sudo apt-get update to update the package list.

    - Next, type `sudo apt-get install build-essential to install the necessary tools for building software, including make.

    - Once the installation is complete, you should be able to use Make in the Linux terminal.

Note that you must be familiar with using a __Linux command-line interface__ to use make on Windows.

#### Installation on Local / Development 
These are steps that one should take towards deploying this project successfully in a local or development environment which could be in a local machine or similar. 

1. Clone the repository to your local machine.
   ```shell
   git clone  https://github.com/jkariukidev/nairobi-busstops.git
   ```
2. Rename the [.env_local.sample](.env_local.sample) file to `.env` to be used by docker.
3. Add the values for the environment variables. One of the reasons for environment variables is to avoid hard-coding passwords and sensitive information on the code. The environment variables include:
   * ``COMPOSE_PROJECT_NAME`` - The name (prefix) for the docker-compose services.
   * ``SECRET_KEY`` - Django cryptography key described in detail [here](https://docs.djangoproject.com/en/4.2/ref/settings/#secret-key).
   * ``DEBUG`` - Variable used in local/development to enable debugging (hence set to ``True`` in development). Read more details [here](https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/#debug).
   * ``ALLOWED_HOSTS`` - List of host/domain names that this Django site can serve. Has been set to `localhost`.
   * ``ENGINE`` - Database backend to use. This project uses PostgreSQL backend by default but can be changed in the environment variables.
   * ``POSTGRES_USER`` - Specifies a user with superuser privileges and a database with the same name. Postgres uses the default user when this is empty.
   * ``POSTGRES_PASSWORD`` - Postgres requires a password to function properly, which is the purpose of this mandatory variable.
   * ``POSTGRES_PORT`` - Network port used by the database is also defined in the docker-compose files.
   * ``POSTGRES_HOST`` - The network host used by the database is also defined in the docker-compose files.
   * ``GIS_DB_USER`` - Specifies a database user to be used in this project separate from the database superuser above.
   * ``GIS_DB_PASSWORD`` - Geodatabase's password.
   * ``GIS_DB_NAME`` - Refers to the geodatabase name.
   * ``DATABASE_URL`` - Defines the database URL schema and other parameters using the [12-factor](http://www.12factor.net/backing-services). A definition of URL schemas for different databases can be read [here](https://github.com/jazzband/dj-database-url#url-schema).
4. Build the required docker images for this project using the command.
   ```shell
   make build-dev
   ```
5. Run the development server on http://127.0.0.1:8000  by running.
   ```shell
   make runserver-dev
   ```
6. Apply migrations to synchronize the database state with the current set of models and migration using.
   ```shell
   make migrate-dev
   ```
   in the event [mywebgis models](onyeshamap/models.py) are altered, one can update migrations which generate the SQL commands for apps by running
   ```shell
   make makemigrations-dev
   ```
7. Load geospatial data into the geodatabase making use of GeoDjango's functionalities.
    ```shell
      make load-geospatial-data-dev
      ```
8. __Optional__: Load initial admin login data making use of [django fixtures](https://docs.djangoproject.com/en/4.2/howto/initial-data/). 
   * Admin - This creates a default superuser (testadmin) and a standard user (testuser). The superuser can log into the Django admin panel and change settings etc.
      ```shell
      make load-admin-data-dev
      ```
9. If skipped the previous step, create your own additional superuser by running.
   ```shell
   make superuser-dev
   ```
10. If populated the database using step 7 above, one can try logging in using the following:
    * Navigate to the admin login URL at http://127.0.0.1:8000/geoadmin/
    * Log in using `geouser` as user and `Ge0Aw3s0menes$` as password. (NOTE: this is the superuser with full privileges on this app)
11. Logs can be monitored by running.
    * `make logs-dev` - Prints log output
    * `make logs-interactive-dev` - Show logs interactively
12. On shutting down the development server, run the following.
    * `make shutdown-dev` which stops the running containers (web and database)
    * `make shutdown-volumes-dev` which stops the running containers and deletes volumes that contain persisted data.

#### Installation on Production
These are steps that one should take towards deploying this project successfully in a production environment which could be in a cloud virtual machine (VM) making the project accessible through the internet. Some variable names are the same as the ones in the development environment and have not been repeated below i.e. database environment variables.

1. Clone this project using `git clone ` command.
      ```shell
     git clone https://github.com/jkariukidev/my-demo-website.git
     ```
  2. Navigate into the cloned project folder and using a terminal/shell or otherwise, rename the [env_prod.sample](.env_prod.sample) to `.env` in production to be recognized by docker.
  3. Edit the environment variables as required and ensure you do not share passwords and security keys with the public. The additional environment variables for production include:
     * ``COMPOSE_PROJECT_NAME`` - The name (prefix) for the docker-compose services.
     * ``DEBUG`` - Must be set to `False` to avoid leaking sensitive project and server information displayed during development.
     * ``ALLOWED_HOSTS`` - List of host/domain names that this Django site can serve. Has been set to your domain otherwise the website may not be accessed.
     * ``USE_CLOUDINARY`` - Variable with a Boolean value that directs the app to use Cloudinary settings for static files management.
     * ``CLOUDINARY_CLOUD_NAME`` - Variable pointing to the name of the cloud provided by [cloudinary](https:://cloudinary.com)
     * ``CLOUDINARY_API_KEY`` - Mandatory API key associated with a given Cloudinary account. Please refer to the [Cloudinary documentation](https://cloudinary.com/documentation/django_integration) for more.
     * ``CLOUDINARY_API_SECRET`` - Secret key associated with the `CLOUDINARY_API_KEY`
     * ``CLOUDINARY_URL`` - Combination of the `CLOUDINARY_API_KEY`, `CLOUDINARY_API_SECRET` and `CLOUDINARY_CLOUD_NAME` which consists of the Cloudinary URL.
     * ``USE_S3`` - Variable with Boolean value that directs the app to use Amazon Web Services (AWS) S3 settings for static files management.
     * ``AWS_ACCESS_KEY_ID`` - AWS access key, as a string.
     * ``AWS_SECRET_ACCESS_KEY`` - AWS access key, as a string.
     * ``AWS_STORAGE_BUCKET_NAME`` - AWS storage bucket name, as a string.
     * ``AWS_S3_CUSTOM_DOMAIN`` - Parameter configured when using AWS CloudFront services.
     * ``AWS_S3_OBJECT_PARAMETERS`` - Set parameters on all AWS S3 objects.
     * ``AWS_LOCATION`` - Path prefix that will be prepended to all uploads to AWS S3.
     * ``USE_WHITENOISE`` - Variable with Boolean value that directs the app to use AWS S3 settings for static files management.
     
  4. Run the docker services for this project using compose in production environment.
     ```
     make runserver
     ```
  5. Propagate models into your database schema using the [migrate command](https://docs.djangoproject.com/en/4.2/ref/django-admin/#migrate). Note
     that this command is being run inside the docker web container. Refer for more on [exec docker command](https://docs.docker.com/engine/reference/commandline/compose_exec/).
     ```
     make migrate
     ```
  6. One can copy the static files using the Django's collectstatic command depending on the static files management settings above. 
        ```
        make collectstatic
        ```
7. Load initial data using the same steps as specified in development section above. Using the `make load-admin-data` and `make load-geospatial-data` commands.
8. Check logs using `make logs` or to view the logs interactively use `make logs-interactive`

For several other commands, view them in the [Makefile](Makefile)

## Usage

  - Creating GeoWeb applications.
  - GIS data management across the web.
  - Geo-visualization 
  - Testing and deployment of GeoWeb applications.
  - Static files assets management using services; Cloudinary, AWS S3 etc.


## Tests
Unit tests are a fundamental part of the testing framework that allows you to verify the correctness of your code at a granular level. Unit tests focus on testing individual components, such as models, views, forms, and utility functions, in isolation to ensure they behave as expected.

Check the [project test](onyeshamap/tests.py) for more. To execute tests, use the following command:
```shell
   make test-project
```

## 💳License

<!-- Mention your project licence here and also link to that file -->

Distributed under the GNU General Public [LICENSE](LICENSE).

## Questions?
Contact me via:
* [My Socials](https://linktr.ee/josephkariuki)
* [My Website](https://josephkariuki.com/contact/)

## References
* [Docker Documentation](https://docs.docker.com/) - DevOps centric especially for development and deployment.
* [Docker Compose Django Example](https://docs.docker.com/samples/django/) - Deployment centric specific to Django projects.
* [GeoDjango Documentation](https://docs.djangoproject.com/en/4.2/ref/contrib/gis/) - WebGIS development using GeoDjango API. 
