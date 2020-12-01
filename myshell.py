import os 
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pizzeria.settings") ## (always same, name of project (not app))

import django
django.setup()

from pizza_app.models import Pizza, Topping, Comment

from django.contrib.auth.models import User
for user in User.objects.all():
    print(user.username, user.id)