from rest_framework import serializers

from .models import Cabinet
from resident.serializers import ResidentSerializer

class CabinetSerializer(serializers.ModelSerializer):
    resident_info = ResidentSerializer(source='resident', read_only=True)
    class Meta:
        model = Cabinet
        fields = ('id', 'resident', 'resident_info', 'cabinet_number', 'color', 'path')