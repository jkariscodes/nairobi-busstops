from django.urls import path
from .views import WebMapView
from djgeojson.views import GeoJSONLayerView
from .models import BusStops

urlpatterns = [
    path('',
         WebMapView.as_view(), name='home'),
    path('data/', GeoJSONLayerView.as_view(
        model=BusStops, properties=(
            'stop_name', 'stop_id', 'stop_lat', 'stop_lon', 'route_1'
        )
    ), name='data'),
]
