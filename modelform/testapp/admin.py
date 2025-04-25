from django.contrib import admin
from testapp.models import Student
class StudentAdmin(admin.ModelAdmin):
    list_display=['name','mark']
admin.site.register(Student,StudentAdmin)

# Register your models here.
