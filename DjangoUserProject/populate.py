import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DjangoUserProject.settings')

import django
django.setup()

from new_app.models import User
from faker import Faker

fakegen = Faker()

def populate(N = 5):
    for entry in range(N):
        fakename = fakegen.name()
        fn = fakename.split()[0]
        ln = fakename.split()[1]
        email = fakegen.email()

        user = User.objects.get_or_create(user_fn=fn, user_ln=ln, user_email=email)[0]

if __name__ == '__main__':
    print('Populating Database...')
    populate(20)
    print('Population Complete')
