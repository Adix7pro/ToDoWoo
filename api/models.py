from django.db import models
from django.utils import timezone
# Create your models here.

class Todo(models.Model):
    STATUS_CHOICES = ('CURRENT','CURRENT'),('COMPLETED','COMPLETED')
    title = models.CharField(max_length=200)
    memo = models.TextField()
    status = models.CharField(choices=STATUS_CHOICES,max_length=200)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title




