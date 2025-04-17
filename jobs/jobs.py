import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jobs.settings')
import django
django.setup()
from faker import Faker
from random import *
from testapp.models import Hydinfo,Puneinfo,Banginfo
fake=Faker()
def phonenumber():
    d1=randint(6,9)
    num=""+str(d1)
    for i in range(9):
        num+=str(randint(0,9))
    return num
def jobs(n):
    for i in range(n):
        fdate=fake.date()
        fcompany=fake.company()
        ftitle=fake.job()
        felgibility=fake.text()
        flocation=fake.address()
        femail=fake.email()
        fphonenumber=phonenumber()
        Hydinfo.objects.get_or_create(date=fdate,company=fcompany,title=ftitle,elgibility=felgibility,location=flocation, email=femail,phonenumber=fphonenumber)
        Banginfo.objects.get_or_create(date=fdate,company=fcompany,title=ftitle,elgibility=felgibility,location=flocation, email=femail,phonenumber=fphonenumber)
        Puneinfo.objects.get_or_create(date=fdate,company=fcompany,title=ftitle,elgibility=felgibility,location=flocation, email=femail,phonenumber=fphonenumber)
n=int(input('enter number of records:'))
jobs(n)
print(f'{n} records inserted sucessfully....')
