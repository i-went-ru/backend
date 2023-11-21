from django.db import models
from django.contrib.auth import get_user_model

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

    def __str__(self) -> str:
        return f'{self.pk} | {self.name} | {self.direction}'

class ResidentPhotos(models.Model):
    resident = models.ForeignKey('Resident', on_delete=models.CASCADE, related_name='photos')
    photo = models.ImageField(upload_to='resident/photos')

    def __str__(self) -> str:
        return f'{self.resident.pk} | {self.resident.name} | {self.pk}'