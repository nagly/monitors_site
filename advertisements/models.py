from django.db import models
import uuid
# Create your models here.
class Ad(models.Model):
    place = models.CharField(max_length=1)
    image = models.ImageField(upload_to='banners')
    url = models.CharField(max_length=100)
    weeks = models.PositiveIntegerField(default=1)
    price = models.FloatField()
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    expiration = models.DateTimeField(null=True, blank=True)

class Buffer(models.Model):
    place = models.CharField(max_length=1)
    image = models.ImageField(upload_to='banners')
    url = models.CharField(max_length=100)
    weeks = models.PositiveIntegerField(default=1)
    price = models.FloatField()
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    expiration = models.DateTimeField(null=True, blank=True)
    unique_id = models.CharField(max_length=100, blank=True, unique=True, default=uuid.uuid4)

class OldOne(models.Model):
    place = models.CharField(max_length=1)
    image = models.ImageField(upload_to='banners')
    url = models.CharField(max_length=100)
    weeks = models.PositiveIntegerField(default=1)
    price = models.FloatField()
    created = models.DateTimeField(auto_now_add=True, auto_now=False)