from django.db import models

class MapPhoto(models.Model):
    x = models.IntegerField()
    y = models.IntegerField()
    color = models.TextField()
    image = models.URLField()