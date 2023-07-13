from __future__ import unicode_literals
from django.db.models import Manager as GeoManager
from django.contrib.gis.db import models


# Create your models here.


class BusStops(models.Model):
    _id = models.IntegerField()
    stop_id = models.CharField(max_length=254)
    stop_name = models.CharField(max_length=254)
    stop_lat = models.CharField(max_length=254)
    stop_lon = models.CharField(max_length=254)
    parent_sta = models.CharField(max_length=254, null=True)
    route_1 = models.CharField(max_length=254, null=True)
    route_2 = models.CharField(max_length=254, null=True)
    route_3 = models.CharField(max_length=254, null=True)
    route_4 = models.CharField(max_length=254, null=True)
    route_5 = models.CharField(max_length=254, null=True)
    route_6 = models.CharField(max_length=254, null=True)
    route_7 = models.CharField(max_length=254, null=True)
    route_8 = models.CharField(max_length=254, null=True)
    route_9 = models.CharField(max_length=254, null=True)
    route_10 = models.CharField(max_length=254, null=True)
    route_11 = models.CharField(max_length=254, null=True)
    route_12 = models.CharField(max_length=254, null=True)
    route_13 = models.CharField(max_length=254, null=True)
    route_14 = models.CharField(max_length=254, null=True)
    route_15 = models.CharField(max_length=254, null=True)
    route_16 = models.CharField(max_length=254, null=True)
    route_17 = models.CharField(max_length=254, null=True)
    route_18 = models.CharField(max_length=254, null=True)
    route_19 = models.CharField(max_length=254, null=True)
    route_20 = models.CharField(max_length=254, null=True)
    route_21 = models.CharField(max_length=254, null=True)
    geom = models.MultiPointField(srid=32737)
    objects = GeoManager()

    def __str__(self):
        return self.stop_name

    class Meta:
        verbose_name = "Bus Stops"
