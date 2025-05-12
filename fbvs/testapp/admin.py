from django.contrib import admin
from testapp.models import Emplooye
class EmplooyeAdmin(admin.ModelAdmin):
    list_display=['eno','esal','ename','eaddr']
admin.site.register(Emplooye,EmplooyeAdmin)
# Register your models here.
