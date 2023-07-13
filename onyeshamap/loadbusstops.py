import os
from django.contrib.gis.utils import LayerMapping
from .models import BusStops

bus_stops_mapping = {
    "_id": "Id",
    "stop_id": "stop_id",
    "stop_name": "stop_name",
    "stop_lat": "stop_lat",
    "stop_lon": "stop_lon",
    "parent_sta": "parent_sta",
    "route_1": "route_1",
    "route_2": "route_2",
    "route_3": "route_3",
    "route_4": "route_4",
    "route_5": "route_5",
    "route_6": "route_6",
    "route_7": "route_7",
    "route_8": "route_8",
    "route_9": "route_9",
    "route_10": "route_10",
    "route_11": "route_11",
    "route_12": "route_12",
    "route_13": "route_13",
    "route_14": "route_14",
    "route_15": "route_15",
    "route_16": "route_16",
    "route_17": "route_17",
    "route_18": "route_18",
    "route_19": "route_19",
    "route_20": "route_20",
    "route_21": "route_21",
    "geom": "MULTIPOINT",
}

stop_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "data/Bus_Stops.shp")
)


def run(verbose=True):
    yangu = LayerMapping(
        BusStops,
        stop_shp,
        bus_stops_mapping,
    )
    yangu.save(strict=True, verbose=verbose)
