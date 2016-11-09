from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin
from .models import CCTV, Bus_Stops

# Register your models here.

class cctvAdmin(LeafletGeoAdmin):
	List_display = ('type', 'longitude', 'latitude', 'st_name')

class stopsAdmin(LeafletGeoAdmin):
	List_display = ('stop_name', 'parent_sta', 'route_1')


admin.site.register(CCTV, cctvAdmin,)
admin.site.register( Bus_Stops, stopsAdmin,)