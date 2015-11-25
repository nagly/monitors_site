from django.db import models
from django.utils.encoding import smart_unicode
# Create your models here.
class Monitor(models.Model):
	url = models.URLField()
	url_hyip_details = models.CharField(max_length=100)
	url_card = models.CharField(max_length=100)

	def __unicode__(self):
		return smart_unicode(self.url)