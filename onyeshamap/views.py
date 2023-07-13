from rest_framework import viewsets

from .models import BusStops

from .serializers import BusStopSerializer


class BusStopViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = BusStops.objects.all()
    serializer_class = BusStopSerializer
