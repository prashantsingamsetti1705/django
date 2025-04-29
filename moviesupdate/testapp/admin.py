from django.contrib import admin
from testapp.models import Student
class StudentAdmin(admin.ModelAdmin):
    List_display=["rdate","movie"
    "hero",
    "heroine"
    ,"rating"]
admin.site.register(Student,StudentAdmin)
# Register your models here.
