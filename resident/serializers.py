from rest_framework import serializers
from taggit.serializers import TagListSerializerField, TaggitSerializer

from .models import Resident, ResidentPhotos, FreeDay, BusyDay

class ResidentPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResidentPhotos
        fields = ('id', 'photo')

class FreeDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = FreeDay
        fields = ('date',)

class BusyDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = BusyDay
        fields = ('date',)

class ResidentSerializer(TaggitSerializer, serializers.ModelSerializer):
    photos = ResidentPhotoSerializer(many=True, read_only=True)
    tags = TagListSerializerField()
    free_days = BusyDaySerializer(many=True, read_only=False)
    busy_days = FreeDaySerializer(many=True, read_only=False)

    class Meta:
        model = Resident
        fields = ('id', 'responsible', 'name', 'description', 'direction', 'floor', 'photos', 'tags', 'busy_days', 'free_days')