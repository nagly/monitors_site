from django.contrib import admin
from hyips.models import Hyip, Hyips_info
# Register your models here.

class HyipAdmin(admin.ModelAdmin):
	class Meta:
		model = Hyip
	list_display = ('id','title','url','created')
admin.site.register(Hyip, HyipAdmin)

class Hyips_infoAdmin(admin.ModelAdmin):
	class Meta:
		model = Hyips_info
	list_display = ('hyip_title','monitor_url','listing_id','status')

	def hyip_title(self, instance):
		return instance.hyip_id.title

	def monitor_url(self, instance):
		return instance.monitor_id.url

admin.site.register(Hyips_info, Hyips_infoAdmin)