import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'modeldummy.settings')

import django
django.setup()

from faker import Faker
from random import *
from testapp.models import Students
fake = Faker()

def phonenumbergen():
	d1 = randint(6,9)
	num = '' + str(d1)
	for i in range(9):
		num += str(randint(0,9))
	return int(num)

def populate(n):
    for i in range(n):
        frollno = fake.random_int(min=1,max=999)
        fname = fake.name()
        fdob = fake.date()
        fmarks = fake.random_int(min=1,max=100)
        femail = fake.email()
        fphone = phonenumbergen()
        Students.objects.get_or_create(rollno=frollno,name=fname,dob=fdob,marks=fmarks,email=femail,phone=fphone)
n = int(input('Enter number of records:'))
populate(n)
print(f'{n} Records inserted successfully.....')