from django.db import models
class Book(models.Model):
    title=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    pages=models.IntegerField()
    price=models.DecimalField(max_digits=5,decimal_places=2)
# Create your models here.
