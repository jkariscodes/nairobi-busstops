from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin
from .models import Bus_Stops

# Register your models here.

class stopsAdmin(LeafletGeoAdmin):
	List_display = ('stop_name', 'parent_sta', 'route_1')


admin.site.register( Bus_Stops, stopsAdmin,)
