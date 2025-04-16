from django.contrib import admin
from .models import Students
class StudentsAdmin(admin.ModelAdmin):
    list_display=('rollno','name','dob','marks','email','phone')
admin.site.register(Students,StudentsAdmin)
# Register your models here.
