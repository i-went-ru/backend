from rest_framework import serializers

from .models import Tour
from user.serializers import UserSerializerFull
from resident.serializers import ResidentSerializer

class TourSerializer(serializers.ModelSerializer):
    guide = UserSerializerFull()
    client = UserSerializerFull()
    residents = serializers.SerializerMethodField()

    def get_residents(self, instance):
        queryset = instance.residents.all().order_by('floor')
        return ResidentSerializer(queryset, many=True).data

    class Meta:
        model = Tour
        fields = ('id', 'importance', 'begin_datetime', 'end_datetime', 'status', 'guide', 'client', 'residents')