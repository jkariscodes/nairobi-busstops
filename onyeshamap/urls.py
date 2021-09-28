from django.conf.urls import include, url
from django.views.generic import TemplateView
from djgeojson.views import GeoJSONLayerView
from .models import BusStops

urlpatterns = [

    url(r'^$', TemplateView.as_view(template_name='webapp1.html'), name='home'),
   # url(r'^data/$', GeoJSONLayerView.as_view(model=CCTV, properties=('descriptio', 'type', 'longitude', 'latitude')), name='data'),
    url(r'^data/$', GeoJSONLayerView.as_view(model=BusStops, properties=('stop_name', 'stop_id', 'stop_lat', 'stop_lon', 'route_1')), name='data')

]
