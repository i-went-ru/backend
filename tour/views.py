from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from datetime import datetime

from .models import Tour
from .serializers import TourSerializer

class TourViewSet(viewsets.ModelViewSet):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer

    @action(detail=False, methods=['get'])
    def upcoming(self, request):
        queryset = Tour.objects.filter(begin_datetime__gte=datetime.now()).order_by('begin_datetime')
        return Response(TourSerializer(queryset, many=True).data)