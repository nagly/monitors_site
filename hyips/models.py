from django.db import models

# Create your models here.
class Hyip(models.Model):
 	title = models.CharField(max_length=100)
 	url = models.URLField()
 	created = models.DateTimeField(auto_now_add=True, auto_now=False)
 		