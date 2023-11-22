from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from .models import User
from .serializers import UserSerializerFull

class UserViewSetFull(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializerFull

    def get_permissions(self):
        self.permission_classes = [IsAdminUser,]
        return super().get_permissions()