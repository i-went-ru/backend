from django.contrib import admin

from .models import Resident
from .models import ResidentPhotos

admin.site.register(Resident)
admin.site.register(ResidentPhotos)