from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class GroupModel(models.Model):
    users = models.ManyToManyField(User, related_name='groupss')
    name = models.CharField(max_length=140)
    description = models.TextField(blank=True, null=True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.name
    