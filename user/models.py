from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

class User(AbstractUser):
    USER_TYPES = (
        ('guest', 'обыватель'),
        ('org', 'организация'),
        ('school', 'учебное заведение'),
    )
    full_name = models.CharField(max_length=200)
    organization = models.CharField(max_length=200)
    phone = PhoneNumberField(null = False, blank = False, unique = True)
    user_type = models.CharField(max_length=6, choices=USER_TYPES)
    REQUIRED_FIELDS = ['full_name', 'organization', 'phone', 'user_type']