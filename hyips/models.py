from django.db import models
from django.utils.encoding import smart_unicode
# Create your models here.
class Hyip(models.Model):
	title = models.CharField(max_length=100)
	url = models.URLField()
	created = models.DateTimeField(auto_now_add=True, auto_now=False)

	def __unicode__(self):
		return smart_unicode(self.title)

class Hyips_info(models.Model):
	hyip_id = models.ForeignKey('Hyip')
	monitor_id = models.ForeignKey('monitors.Monitor')
	listing_id = models.CharField(max_length=50)
	status = models.CharField(max_length=1)

	def hyip_title(self):
		return self.hyip_id.title

	def monitor_url(self):
		return self.monitor_id.url