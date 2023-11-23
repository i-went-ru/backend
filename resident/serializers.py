from django.contrib.auth import get_user_model

from rest_framework import serializers
from taggit.serializers import TagListSerializerField, TaggitSerializer

from .models import Resident, ResidentPhotos, FreeDay, BusyDay, ExtraFile
from user.serializers import UserSerializerFull

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

class ExtraFilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtraFile
        fields = ('file',)

class ResponsibleSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('full_name', 'organization', 'phone')

class ResidentSerializer(TaggitSerializer, serializers.ModelSerializer):
    photos = ResidentPhotoSerializer(many=True, read_only=True)
    tags = TagListSerializerField()
    free_days = BusyDaySerializer(many=True, read_only=False, required=False)
    busy_days = FreeDaySerializer(many=True, read_only=False, required=False)
    extra_files = ExtraFilesSerializer(many=True, read_only=True)
    responsible_info = ResponsibleSerializer(source='responsible')

    class Meta:
        model = Resident
        fields = ('id', 'responsible', 'responsible_info', 'name', 'description', 'direction', 'floor', 'photos', 'tags', 'busy_days', 'free_days', 'extra_files')