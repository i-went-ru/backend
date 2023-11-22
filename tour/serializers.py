from rest_framework import serializers

from .models import Tour
from user.serializers import UserSerializerFull

class TourSerializer(serializers.ModelSerializer):
    guide = UserSerializerFull()
    client = UserSerializerFull()
    class Meta:
        model = Tour
        fields = ('guide', 'client', 'datetime', 'status')