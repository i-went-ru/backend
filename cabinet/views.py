from rest_framework import viewsets

from .models import Cabinet
from .serializers import CabinetSerializer

class CabinetViewSet(viewsets.ModelViewSet):
    queryset = Cabinet.objects.all()
    serializer_class = CabinetSerializer