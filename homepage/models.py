from django.db import models
from django.utils import timezone
from custom_user.models import MyUser


class Bugs(models.Model):
    class Status(models.TextChoices):
        NEW = 'NEW'
        IN_PROGRESS = 'IN PROGRESS'
        DONE = 'DONE'
        INVALID = 'INVALID'
    title = models.CharField(max_length=50)
    created = models.DateField(default=timezone.now)
    description = models.TextField()
    filed_by = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    status = models.CharField(max_length=12, choices=Status.choices, default=Status.NEW)
    assigned_to = models.ForeignKey(MyUser, related_name='user_assigned', on_delete=models.SET_NULL, blank=True, null=True)
    completed_by = models.ForeignKey(MyUser, related_name='user_completed', on_delete=models.SET_NULL, blank=True, null=True)

    @property
    def ticket_age(self):
        start_date = timezone.datetime.strptime(str(self.created), '%Y-%m-%d')
        str_time = str(timezone.now())
        num_char = len(str_time)-6
        str_time = str_time[:num_char]
        end_date = timezone.datetime.strptime(str_time, '%Y-%m-%d %H:%M:%S.%f')
        return abs((end_date - start_date).days)







