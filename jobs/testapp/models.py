from django.db import models
class Hydinfo(models.Model):
    date=models.DateField()
    company=models.CharField(max_length=100)
    title=models.CharField(max_length=100)
    elgibility=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    email=models.EmailField()
    phonenumber=models.CharField(max_length=100)
#pune
class Puneinfo(models.Model):
    date=models.DateField()
    company=models.CharField(max_length=100)
    title=models.CharField(max_length=100)
    elgibility=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    email=models.EmailField()
    phonenumber=models.CharField(max_length=100)
#banglore
class Banginfo(models.Model):
    date=models.DateField()
    company=models.CharField(max_length=100)
    title=models.CharField(max_length=100)
    elgibility=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    email=models.EmailField()
    phonenumber=models.CharField(max_length=100)


# Create your models here.
