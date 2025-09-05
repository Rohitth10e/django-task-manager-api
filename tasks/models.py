from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class task(models.Model):
    '''Model for tasks'''
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')

    def __str__(self):
        return f"task {self.title} created at {self.created_at} by user {self.owner}"