from rest_framework import serializers

from .models import Cabinet

class CabinetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cabinet
        fields = ('id', 'resident', 'cabinet_number', 'color', 'path')