from django.db import models

class Cabinet(models.Model):
    resident = models.ForeignKey('resident.Resident', on_delete=models.SET_NULL, null=True, blank=True)
    cabinet_number = models.CharField(max_length=3, blank=False)
    path = models.TextField(blank=False)
    color = models.TextField(blank=False)