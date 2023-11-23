from rest_framework import viewsets

from .models import MapPhoto
from .serializers import MapPhotoSerializer

class MapPhotoViewSet(viewsets.ModelViewSet):
    queryset = MapPhoto.objects.all()
    serializer_class = MapPhotoSerializer