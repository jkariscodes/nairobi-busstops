import os
from django.contrib.gis.utils import LayerMapping
from .models import CCTV

cctv_mapping = {
    'objectid' : 'OBJECTID',
    'type' : 'Type',
    'longitude' : 'Longitude',
    'latitude' : 'Latitude',
    'eastings' : 'Eastings',
    'northings' : 'Northings',
    'st_name' : 'ST_NAME',
    'descriptio' : 'Descriptio',
    'geom' : 'MULTIPOINT',
}

cctv_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),'data/CCTV_Location.shp'))
def run(verbose=True):
	yetu = LayerMapping(CCTV, cctv_shp, cctv_mapping, )
	yetu.save(strict=True, verbose=verbose)