from django.db import models
class employess(models.Model):
    emp_id=models.IntegerField()
    emp_name=models.CharField(max_length=20)
    emp_sal=models.IntegerField(max_length=10)
    emp_addr=models.CharField(max_length=30)
# Create your models here.
