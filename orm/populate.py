import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'orm.settings')
import django
django.setup()
from testapp.models import Employee
from faker import Faker
from random import *
faker=Faker()
def populate(n):
    for i in range(n):
        feno=randint(1,100)
        fname=faker.name()
        fesal=randint(1,1000000)
        faddr=faker.address()
        emp=Employee.objects.get_or_create(eno=feno,ename=fname,esal=fesal,eaddr=faddr)
n=int(input("Enter the number of records you want to insert: "))
populate(n)
print("data insterted sucessfully")
