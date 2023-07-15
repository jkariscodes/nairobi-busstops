from django.urls import path
from .views import BusStopViewSet
from djgeojson.views import GeoJSONLayerView
from .models import BusStops

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(prefix="busstops", viewset=BusStopViewSet, basename="busstops")

urlpatterns = router.urls
