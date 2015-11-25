from django.contrib import admin
from monitors.models import Monitor
# Register your models here.
class MonitorAdmin(admin.ModelAdmin):
	class Meta:
		model = Monitor
	list_display = ('url','url_hyip_details','url_card')
admin.site.register(Monitor, MonitorAdmin)