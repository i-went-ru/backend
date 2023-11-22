from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Tour(models.Model):
    STATUSES = (
        ('canceled', 'отменён'),
        ('moderation', 'в модерации'),
        ('approved', 'одобрен'),
        ('notapproved', 'не одобрен'),
    )
    guide = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='guided_tours')
    client = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='tours')
    datetime = models.DateTimeField(unique=True)
    status = models.CharField(max_length=11, choices=STATUSES)
    comment = models.CharField(max_length=2500)

    def __str__(self) -> str:
        return f'{self.pk} | {self.datetime} | {self.status}'