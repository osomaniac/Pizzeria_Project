import os 
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pizzeria.settings") ## (always same, name of project (not app))

import django
django.setup()

from pizza_app.models import Pizza, Topping, Comment

'''
from django.contrib.auth.models import User
for user in User.objects.all():
    print(user.username, user.id)
'''

toppings = Topping.objects.all()
pizzas = Pizza.objects.all()

for t in toppings:
    print("Topping ID", t.id, " ->  Topping:", t, " ->  Image Path: ", t.image_path )

for p in pizzas:
    print("Pizza ID", p.id, " ->  Pizza:", p, " ->  Image Path: ", p.image_path )
