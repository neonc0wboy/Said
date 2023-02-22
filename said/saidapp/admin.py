from django.contrib import admin


# Register your models here
from django.contrib import admin
from .models import product, Market, Employee, Client, Order

admin.site.register(product)
admin.site.register(Market)
admin.site.register(Employee)
admin.site.register(Client)
admin.site.register(Order)
