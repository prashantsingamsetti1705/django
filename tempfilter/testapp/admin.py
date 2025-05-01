from django.contrib import admin
from testapp.models import StudentModel
class StudentAdmin(admin.ModelAdmin):
    list_display=['name','subject','dept','date']
admin.site.register(StudentModel,StudentAdmin)

# Register your models here.
