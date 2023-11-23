from django.contrib import admin

from .models import Resident, ResidentPhotos, FreeDay, BusyDay

admin.site.register(Resident)
admin.site.register(ResidentPhotos)
admin.site.register(FreeDay)
admin.site.register(BusyDay)