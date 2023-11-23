from rest_framework import serializers

from .models import Tour
from user.serializers import UserSerializerFull
from resident.serializers import ResidentSerializer

class TourSerializer(serializers.ModelSerializer):
    guide_info = UserSerializerFull(source='guide', read_only=True)
    client_info = UserSerializerFull(source='client', read_only=True)
    residents_info = serializers.SerializerMethodField()

    begin_datetime = serializers.DateTimeField(required=True)
    end_datetime = serializers.DateTimeField(required=True)
    status = serializers.CharField(required=True)

    def get_residents_info(self, instance):
        queryset = instance.residents.all().order_by('floor')
        return ResidentSerializer(queryset, many=True).data

    class Meta:
        model = Tour
        fields = ('id', 'importance', 'guest_count', 'begin_datetime', 'end_datetime', 'status', 'format', 'comment', 'guide', 'guide_info', 'client', 'client_info', 'residents', 'residents_info')