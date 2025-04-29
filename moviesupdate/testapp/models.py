from django.db import models
class Student(models.Model):
    rdate=models.DateField()
    movie=models.CharField(max_length=30)
    hero=models.CharField(max_length=30)
    heroine=models.CharField(max_length=30)
    rating=models.IntegerField()
# Create your models here.
