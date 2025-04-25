from django.db import models
class Student(models.Model):
    name=models.CharField(max_length=30)
    mark=models.IntegerField()
# Create your models here.
