from django.db import models

class MapPhoto(models.Model):
    x = models.FloatField()
    y = models.FloatField()
    color = models.TextField()
    image = models.URLField()