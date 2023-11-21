from rest_framework import viewsets

from .models import Resident
from .serializers import ResidentSerializer

class ResidentViewSet(viewsets.ModelViewSet):
    queryset = Resident.objects.all()
    serializer_class = ResidentSerializer