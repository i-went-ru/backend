from typing import override
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .models import Resident
from .serializers import ResidentSerializer, ResidentPhotoSerializer

class ResidentViewSet(viewsets.ModelViewSet):
    queryset = Resident.objects.all()
    serializer_class = ResidentSerializer

    
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name='tags',
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                description='Comma-separated list of tags',
                required=False,
            ),
        ],
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        tags_string = self.request.query_params.get('tags', '')
        if tags_string:
            tags = tags_string.split(',')
            queryset = queryset.filter(tags__name__in=tags)
        return queryset

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated], serializer_class=ResidentPhotoSerializer)
    def add_photo(self, request, pk=None):
        resident: Resident = self.get_object()
        resident.add_photo(request.user, request.data['photo'])
        return Response('successfully added a new photo')