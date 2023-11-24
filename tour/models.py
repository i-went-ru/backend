from django.db import models
from django.contrib.auth import get_user_model

from rest_framework.exceptions import ValidationError

from resident.models import Resident

User = get_user_model()

class Tour(models.Model):
    STATUSES = (
        ('canceled', 'отменён'),
        ('moderation', 'в модерации'),
        ('approved', 'одобрен'),
        ('notapproved', 'не одобрен'),
        ('sended', 'отправлено'),
    )

    FORMATS = (
        ('overwiew', 'Обзорная экскурсия'),
        ('education', 'Образовательная экскурсия'),
        ('exhibition', 'Экспозиционные мероприятия'),
        ('buisiness', 'Бизнес-тур для инвесторов'),
        ('profile', 'Профильные'),
    )

    guide = models.ForeignKey(User, null=True, blank=False, on_delete=models.SET_NULL, related_name='guided_tours')
    client = models.ForeignKey(User, null=True, blank=False, on_delete=models.SET_NULL, related_name='client_tours')
    guest_count = models.IntegerField(blank=False)
    begin_datetime = models.DateTimeField(unique=True, null=True)
    end_datetime = models.DateTimeField(unique=True, null=True)
    status = models.CharField(max_length=11, choices=STATUSES, default='sended')
    format = models.CharField(max_length=11, choices=FORMATS)
    comment = models.CharField(max_length=2500, blank=True, null=True)
    residents = models.ManyToManyField(Resident, related_name='resident_tours', blank=False)

    # properties
    @property
    def importance(self):
        if self.client.user_type == 'org': # type: ignore
            return 'high'
        return 'medium'
    
    # actions (should work)
    def change_begin_datetime(self, datetime):
        if not datetime:
            return ValidationError('datetime required')
        self.begin_datetime = datetime
    
    def change_end_datetime(self, datetime):
        if not datetime:
            return ValidationError('datetime required')
        self.end_datetime = datetime

    def change_guests_count(self, amount):
        if not amount:
            return ValidationError('amount required')
        self.guest_count = amount
    
    def change_guide(self, user):
        if not user:
            return ValidationError('user required')
        self.guide = user
    
    def change_status(self, status):
        if not status:
            return ValidationError('status required')
        if not (status in self.STATUSES):
            return ValidationError(f'{status} not in statuses list')
        self.status = status
    
    def add_resident(self, resident):
        if not resident:
            return ValidationError('resident required')
        if resident.user_type != 'resident':
            return ValidationError(f'{resident} not resident')
        self.residents.add(resident)
    
    def delete_resident(self, resident):
        if not resident:
            return ValidationError('resident required')
        if not (resident in self.residents):
            return ValidationError(f'{resident} not in residents list')
        self.residents.remove(resident)

    def __str__(self) -> str:
        return f'{self.pk} | {self.begin_datetime} — {self.end_datetime} | {self.status}'