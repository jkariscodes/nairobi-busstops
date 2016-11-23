# djangoleaflet webapp

A simple Web GIS application developed in Django and Leaflet

First, download and install PostgreSQL and Python

#Repo
Clone the repository 
>> git clone https://github.com/joehene/djangoleaflet.git

>> cd djangoleaflet

Install python packages using pip
>> pip install -r requirements.txt

#Configuring Django Project 
>> python manage.py createsuperuser

>> python manage.py runserver

makemigrations into your database (postgreSQL with postgis used)
>> python manage.py makemigrations

>> python manage.py migrate

#Adding Datas
>> python manage.py shell

 
>>from onyeshamap import loadbusstops
>>loadbusstops.run()
>>exit()


>> python manage.py runserver

navigate to http://localhost:8000/data to view the GeoJSON on browser
Leaflet map showing busstops location at http://localhost:8000



