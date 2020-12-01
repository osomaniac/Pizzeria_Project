from django.contrib import admin

# Register your models here.
from .models import Pizza
admin.site.register(Pizza)

from .models import Topping
admin.site.register(Topping)