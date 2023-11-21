from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Resident
from .serializers import ResidentSerializer, ResidentPhotoSerializer

class ResidentViewSet(viewsets.ModelViewSet):
    queryset = Resident.objects.all()
    serializer_class = ResidentSerializer

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated], serializer_class=ResidentPhotoSerializer)
    def add_photo(self, request, pk=None):
        resident: Resident = self.get_object()
        resident.add_photo(request.user, request.data['photo'])
        return Response('successfully added a new photo')