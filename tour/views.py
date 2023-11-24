from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from datetime import datetime, timedelta

from .models import Tour
from .serializers import TourSerializer

class TourViewSet(viewsets.ModelViewSet):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        status = self.request.query_params.get('status', '') # type: ignore
        if status:
            queryset = queryset.filter(status=status)
        return queryset

    @action(detail=False, methods=['get'])
    def upcoming(self, request):
        queryset = Tour.objects.filter(begin_datetime__gte=datetime.now()).filter(status='approved').order_by('begin_datetime')
        return Response(TourSerializer(queryset, many=True).data)
    
    @action(detail=False, methods=['get'], url_path='upcoming/week')
    def upcoming_week(self, request):
        today = datetime.now().date()
        week_from_now = today + timedelta(weeks=1)
        queryset = Tour.objects.filter(begin_datetime__range=[today, week_from_now]).filter(status='approved').order_by('begin_datetime')
        return Response(TourSerializer(queryset, many=True).data)
    
    @action(detail=False, methods=['get'], url_path='upcoming/month')
    def upcoming_month(self, request):
        today = datetime.now().date()
        month_from_now = today + timedelta(days=30)
        queryset = Tour.objects.filter(begin_datetime__range=[today, month_from_now]).filter(status='approved').order_by('begin_datetime')
        return Response(TourSerializer(queryset, many=True).data)