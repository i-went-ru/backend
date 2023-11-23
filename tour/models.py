from django.db import models
from django.contrib.auth import get_user_model
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

    guide = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='guided_tours')
    client = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='client_tours')
    guest_count = models.IntegerField(blank=False)
    begin_datetime = models.DateTimeField(unique=True, null=True)
    end_datetime = models.DateTimeField(unique=True, null=True)
    status = models.CharField(max_length=11, choices=STATUSES, default='moderation')
    comment = models.CharField(max_length=2500, blank=True, null=True)
    residents = models.ManyToManyField(Resident, related_name='resident_tours', blank=True)

    # properties
    @property
    def importance(self):
        if self.client.user_type == 'org': # type: ignore
            return 'high'
        return 'medium'
    
    # actions
    def change_begin_datetime(self, datetime):
        # TODO
        pass
    
    def change_end_datetime(self, datetime):
        # TODO
        pass

    def change_guests_count(self, amount):
        # TODO
        pass
    
    def change_guide(self, user):
        # TODO
        pass
    
    def change_status(self, status):
        # TODO
        pass
    
    def add_resident(self, resident):
        # TODO
        pass
    
    def delete_resident(self, resident):
        # TODO
        pass

    def __str__(self) -> str:
        return f'{self.pk} | {self.begin_datetime} — {self.end_datetime} | {self.status}'