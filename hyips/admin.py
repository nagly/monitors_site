from django.contrib import admin
from hyips.models import Hyip
# Register your models here.

class HyipAdmin(admin.ModelAdmin):
	class Meta:
		model = Hyip
	list_display = ('id','title','url','created')
admin.site.register(Hyip, HyipAdmin)