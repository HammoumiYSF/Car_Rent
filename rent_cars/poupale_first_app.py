import os
os.environ.setdefault("django_setting_models","first_app.setting")
import django
django.setup()
from first_app.models import login
from faker import Faker

Fake_gen=Faker()

def population(N=6):
    for en in range(N):
        fake_name=Fake_gen.name().split()
        Fake_first_name=fake_name[0]
        Fake_Last_name=fake_name[1]
        Fake_Email=Fake_gen.email()

        login=login.objects.get_or_create(first_name=Fake_first_name,
                                          Last_name=Fake_Last_name,
                                          Email=Fake_Email[0])

if __name__="__main__":
    print("POPULATING DATABASES")
    population(20)
    print("Complete !!")
    
