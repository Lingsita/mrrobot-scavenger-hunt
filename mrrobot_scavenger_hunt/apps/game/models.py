from django.contrib.auth.models import User
from django.db import models

class Game(models.Model):
    IN_PROGRESS = 'in_progress'
    FINISHED = 'finished'
    STATUS_CHOICES = (
        (IN_PROGRESS, 'In Progress'),
        (FINISHED, 'Finished'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField('Score', null=True, blank=True)
    status = models.CharField(
        max_length=11,
        choices=STATUS_CHOICES,
        default=IN_PROGRESS
    )
    email = models.EmailField()
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(blank=True, null=True)