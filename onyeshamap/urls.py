from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from djgeojson.views import GeoJSONLayerView
from .models import CCTV #Bus_Stops

urlpatterns = [

    url(r'^$', TemplateView.as_view(template_name='webapp1.html'), name='home'),
    url(r'^data/$', GeoJSONLayerView.as_view(model=CCTV, properties=('descriptio', 'type', 'longitude', 'latitude')), name='data'),
    #url(r'^data/stops$', GeoJSONLayerView.as_view(model=Bus_Stops, properties=('stop_name', 'stop_id', 'stop_lat', 'stop_lon', 'route_1')), name='data2')

]