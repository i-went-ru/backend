from rest_framework import serializers

from .models import Tour
from user.serializers import UserSerializerFull
from resident.serializers import ResidentSerializer

class TourSerializer(serializers.ModelSerializer):
    guide = UserSerializerFull()
    client = UserSerializerFull()
    residents = ResidentSerializer(many=True)

    class Meta:
        model = Tour
        fields = ('id', 'datetime', 'status', 'guide', 'client', 'residents')