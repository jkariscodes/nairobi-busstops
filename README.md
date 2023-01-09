# Nairobi Bus Stops WebMap 

![image](https://user-images.githubusercontent.com/23359514/183810750-2aaad2ef-1f9c-4637-a572-f1cf353e12c7.png)


A simple Web GIS application developed in Django and Leaflet. This app renders bus stops from the database and parses
them into GeoJSON which are then displayed in the web map.

# Requirements
1. Python - https://www.python.org/downloads/
2. PostgreSQL - https://www.postgresql.org/download/
3. PostGIS - https://postgis.net/install/ 
4. Docker (optional but fast to deploy). - https://docs.docker.com/get-docker/ 

Dependencies include:
* [Django](https://www.djangoproject.com/) - Python web framework used to serve the data stored in database in a web page.
* [Psycopg2](https://www.psycopg.org/) - Python-based database adapter used to connect and support database operations
* [Whitenoise](http://whitenoise.evans.io/en/stable/) - Third-party library that supports serving of static files in Django-based apps.

### Cloning the Repository
Clone the repository 
>> git clone https://github.com/jkariukidev/djangoleaflet.git

>> cd djangoleaflet

Install python packages using pip
>> pip install -r requirements.txt

### Configuring Django Project

>> python manage.py runserver

##### makemigrations into your database (PostgreSQL with PostGIS used)

>> python manage.py migrate

### Create admin user

>> python manage.py createsuperuser

### Adding Models from Dataset
If using different dataset with a different model. The mapping in [models.py](onyeshamap/models.py) has to be changed.
>> python manage.py shell

```
    from onyeshamap import loadbusstops

    loadbusstops.run()

    exit()
```
Run the development server.
>> python manage.py runserver

Raw JSON data can be viewed at http://localhost:8000/data

Map can be viewed at http://localhost:8000

## Docker Deployment
### Environment variables
After cloning the project and assuming docker is installed, create and environment variable file. A [sample .env file]()
has been provided here. It contains:
* `ENVIRONMENT` - Variable referring to the environment of running this project, whether development or production. The default
in [settings.py](mywebgis/settings.py#L6) is `production` but can be changed. Note that `development` is for testing purpose.
* `SECRET_KEY` - Django cryptographic signing key created when one creates a Django project. Refer [documentation](https://docs.djangoproject.com/en/4.0/ref/settings/#secret-key)
for details.
* `DEBUG` - Boolean variable that if set `TRUE` or `1` shows detialed error if encountered and important during development
otherwise in a production environment it should striclty be set to `False` or `0`. More reference [here](https://docs.djangoproject.com/en/4.0/ref/settings/#debug).
* `POSTGRES_DB` - The default database produced when the image is first started might have a different name defined using 
this optional environment variable. If it is not supplied, `POSTGRES USER`'s value will be applied.
* `POSTGRES_USER` - In order to set a user and password, you can use this optional environment variable along with POSTGRES PASSWORD.
This variable will create a database with the same name and grant superuser privileges to the specified user.
The Postgres default user will be used if it is not given. 
* `POSTGRES_PASSWORD` - You must have this environment variable set in order to utilize the PostgreSQL image.
It cannot be blank or undefinable.
For PostgreSQL, this environment variable controls the superuser password.
The `POSTGRES USER` environment setting specifies the superuser by default. 
* `POSTGRES_PORT` - Explicit TCP port number for the PostgreSQL/PostGIS database.
* `POSTGRES_HOST` - The hostname or IP of the database however, it is set to the name of the container running the database service.

For more on PostgreSQL variables, refer to [PostgreSQL on Docker](https://hub.docker.com/_/postgres/).
### Starting Services
There are two services in this project under docker. They include Web and Database services. 
#### Web service
Consists of the initially created Django project and applications that are coded in this project. This service is dependent 
on the database service. It is defined in the [docker configuration](docker-compose.yml).
#### Database service
This service manages a PostGIS instance which is a PostgreSQL container having PostGIS extension installed to facilitate 
handling of spatial/GIS/location data. It is defined in the [docker configuration](docker-compose.yml).

Run `docker-compose up -d` to run build and start the containers. The `-d` switch instructs docker to run the oontainers 
in 'detached' mode i.e. in the background such that you can use terminal or shell to do other things. You can make use of 
[Docker Desktop](https://www.docker.com/products/docker-desktop/) which has a user-friendly dashboard showing containers, 
images, volumes and their statuses among other things. A screenshot of the dashboard is as shown below.

### Stopping Services
To gracefully stop the services, one can make use of the Docker Desktop or alternatively run the folloing command while 
in project directory. 
`docker compose down` and if one wants to remove the persisted data (volumes) run `docker compose down -v`

## Heroku Deployment
This project makes use of [heroku YAML file](heroku.yml) for deployment synonymous to docker. Please refer to [Heroku 
documentation](https://devcenter.heroku.com/articles/build-docker-images-heroku-yml) for more details.

## Questions
Contact me via:
* [My Socials](https://linktr.ee/josephkariuki)
* [My Website](https://josephkariuki.com/)

## References
* [Docker Documentation](https://docs.docker.com/) - DevOps centric especially for development and deployment.
* [Docker Compose Django Example](https://docs.docker.com/samples/django/) - Deployment centric specific to Django projects.
* [GeoNode Documentation](https://docs.geonode.org/en/master/index.html) - WebGIS development and deployment. 




