from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import BusStops


class BusStopSerializer(GeoFeatureModelSerializer):
    """A class to serialize locations as GeoJSON compatible data"""

    class Meta:
        model = BusStops
        geo_field = "geom"
        fields = ("_id", "stop_id", "stop_name", "stop_lat", "stop_lon")
