from django.contrib import admin
from hyips_info.models import Hyips_info
# Register your models here.
class Hyips_infoAdmin(admin.ModelAdmin):
	class Meta:
		model = Hyips_info
	list_display = ('hyip_title','monitor_url','listing_id','status')

	def hyip_title(self, instance):
		return instance.hiyp_id.hiyp_title

	def monitor_url(self, instance):
		return instance.monitor_id.url

admin.site.register(Hyips_info, Hyips_infoAdmin)