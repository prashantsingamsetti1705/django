from django.contrib import admin
from testapp.models import Hydinfo,Puneinfo,Banginfo
# Register your models here.
class HydinfoAdmin(admin.ModelAdmin):
    list_display=('date','company','title','elgibility','location','email','phonenumber')
admin.site.register(Hydinfo,HydinfoAdmin)
class PuneinfoAdmin(admin.ModelAdmin):
    list_display=('date','company','title','elgibility','location','email','phonenumber')
admin.site.register(Puneinfo,PuneinfoAdmin)
class BanginfoAdmin(admin.ModelAdmin):
    list_display=('date','company','title','elgibility','location','email','phonenumber')
admin.site.register(Banginfo,BanginfoAdmin)