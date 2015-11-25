from django.db import models

# Create your models here.
class Hyips_info(models.Model):
	hyip_id = models.ForeignKey('hyips.Hyip')
	monitor_id = models.ForeignKey('monitors.Monitor')
	listing_id = models.CharField(max_length=50)
	status = models.CharField(max_length=1)

	def hyip_title(self):
		return self.hyip_id.hyip_title

	def monitor_url(self):
		return self.monitor_id.url
