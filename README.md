# djangoleaflet webapp 

A simple Web GIS application developed in Django and Leaflet. This app renders busstops from the database and parses
them into GeoJSON which are then displayed in the web map.

First, download and install PostgreSQL and Python

### Cloning the Repository
Clone the repository 
>> git clone https://github.com/jkariukidev/djangoleaflet.git

>> cd djangoleaflet

Install python packages using pip
>> pip install -r requirements.txt

### Configuring Django Project

>> python manage.py runserver

##### makemigrations into your database (postgreSQL with postgis used)

>> python manage.py makemigrations

>> python manage.py migrate

### Create admin user

>> python manage.py createsuperuser

### Adding Models from Dataset
>> python manage.py shell
 
>> from onyeshamap import loadbusstops

>> loadbusstops.run()

>> exit()

>> python manage.py runserver

navigate to http://localhost:8000/data to view the raw GeoJSON data

Leaflet map showing bus stops locations can be viewed at http://localhost:8000

![Alt text](https://github.com/joehene/djangoleaflet/blob/master/onyeshamap/map_display.png?raw=true "Map")

![Alt text](https://github.com/joehene/djangoleaflet/blob/master/onyeshamap/geojson_raw.png?raw=true "GeoJSON")

## Built With

* [leaflet](https://leafletjs.com/) - Web Map 
* [Django](https://www.djangoproject.com/) - Web Framework used
* [PostGIS](https://postgis.net/documentation/) - Database used
