from django.db import models

# Create your models here.


class Room(models.Model):
    name = models.CharField(max_length=255)


class Message(models.Model):
    msg = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    room = models.CharField(max_length=255)
    user = models.CharField(max_length=255)

