from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin
from .models import BusStops


# Register your models here.


class BusStopsAdmin(LeafletGeoAdmin):
    List_display = ("stop_name", "parent_sta", "route_1")


admin.site.register(
    BusStops,
    BusStopsAdmin,
)
