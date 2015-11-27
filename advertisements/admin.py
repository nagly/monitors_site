from django.contrib import admin
from advertisements.models import Ad, Buffer, OldOne
# Register your models here.
class AdAdmin(admin.ModelAdmin):
    class Meta:
        model = Ad
    list_display = ('id', 'place', 'url', 'created', 'price',)
    #readonly_fields = ('created','expiration',)
admin.site.register(Ad, AdAdmin)

class BufferAdmin(admin.ModelAdmin):
    class Meta:
        model = Buffer
    list_display = ('id', 'place', 'url', 'created', 'price',)
    #readonly_fields = ('created','expiration',)
admin.site.register(Buffer, BufferAdmin)

class OldOneAdmin(admin.ModelAdmin):
    class Meta:
        model = OldOne
    list_display = ('id', 'place', 'url', 'created', 'price',)
    #readonly_fields = ('created','expiration',)
admin.site.register(OldOne, OldOneAdmin)