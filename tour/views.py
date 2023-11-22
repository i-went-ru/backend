from rest_framework import viewsets
from datetime import datetime

from .models import Tour
from .serializers import TourSerializer

class TourViewSet(viewsets.ModelViewSet):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer

    def upcoming(self):
        queryset = Tour.objects.filter(begin_datetime - datetime.now() > 0).order_by('begin_datetime')
        return TourSerializer(queryset, many=True).data