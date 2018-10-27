import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'user_management.settings')

import django

django.setup()

from userinfoapp.models import User
from faker import Faker

fake = Faker()

def populate(N=5):
    for entry in range(N):
        fake_name = fake.name()
        fake_firstname = fake_name.split()[0]
        fake_lastname = fake_name.split()[1]
        fake_emailid = fake.email()

        User.objects.get_or_create(firstname = fake_firstname, lastname = fake_lastname, emaild = fake_emailid)[0]

if __name__ == '__main__':
    print("Start populating")
    populate(6)
    print("Completed")
