from django.db import models
class Emplooye(models.Model):
    eno=models.IntegerField()
    esal=models.IntegerField()
    ename=models.CharField(max_length=64)
    eaddr=models.CharField(max_length=100)
# Create your models here.
