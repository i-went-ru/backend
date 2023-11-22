from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator

from rest_framework.exceptions import bad_request
from taggit.managers import TaggableManager

User = get_user_model()

class Resident(models.Model):
    DIRECTIONS = (
        ('it', 'ИТ'),
        ('production', 'производство'),
        ('energy_efficiency', 'энергоэффективность'),
        ('bio_technologies', 'биотехнологии'),
        ('building', 'строительство'),
    )
    responsible = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=2500)
    direction = models.CharField(max_length=17, choices=DIRECTIONS)
    floor = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(12)]
    )
    tags = TaggableManager()

    def add_photo(self, user, image):
        if user != self.responsible:
            return bad_request
        if not image:
            return bad_request
        
        new_photo = ResidentPhotos()
        new_photo.resident = self
        new_photo.photo = image
        new_photo.save()
        

    def __str__(self) -> str:
        return f'{self.pk} | {self.name} | {self.direction}'

class ResidentPhotos(models.Model):
    resident = models.ForeignKey('Resident', on_delete=models.CASCADE, related_name='photos')
    photo = models.ImageField(upload_to='residents/photos')

    def __str__(self) -> str:
        return f'{self.resident.pk} | {self.resident.name} | {self.pk}'