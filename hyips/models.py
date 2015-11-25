from django.db import models
from django.utils.encoding import smart_unicode
# Create your models here.
class Hyip(models.Model):
	title = models.CharField(max_length=100)
	url = models.URLField()
	created = models.DateTimeField(auto_now_add=True, auto_now=False)

	def __unicode__(self):
		return smart_unicode(self.title)