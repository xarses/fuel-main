from django.db import models
from django.contrib.auth.models import User
from jsonfield import JSONField


class Environment(models.Model):
    #user = models.ForeignKey(User, related_name='environments')
    name = models.CharField(max_length=100)


class Role(models.Model):
    id = models.CharField(max_length=30, primary_key=True)
    name = models.CharField(max_length=50)


class Node(models.Model):
    NODE_STATUSES = (
        ('online', 'online'),
        ('offline', 'offline'),
        ('busy', 'busy'),
    )
    id = models.CharField(max_length=12, primary_key=True)
    environment = models.ForeignKey(Environment, related_name='nodes',
        null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=100, null=True, blank=True)
    status = models.CharField(max_length=30, choices=NODE_STATUSES,
            default='online')
    metadata = JSONField()
    roles = models.ManyToManyField(Role, related_name='nodes')
