from django.contrib import admin
from .models import *
# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    filter_horizontal = ['pizzas', ]
    readonly_fields = ['pizzas', ]

admin.site.register(Pizza)
admin.site.register(InstancePizza)
admin.site.register(Order, OrderAdmin)