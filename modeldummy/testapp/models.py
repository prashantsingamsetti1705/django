from django.db import models
class Students(models.Model):
    rollno=models.IntegerField()
    name=models.CharField(max_length=100)
    dob=models.DateField()
    marks=models.IntegerField()
    email=models.EmailField()
    phone=models.CharField(max_length=10)
    #reate your models here.
