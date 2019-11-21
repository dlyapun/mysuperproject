from django.db import models
from accounts.models import User

# Create your models here.
class MySuperModel(models.Model):
    token = models.CharField(max_length=300, null=True, blank=True)
    create_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    expiration_date = models.DateTimeField(null=True, blank=True)
    changed = models.BooleanField(default=False)
    name = models.CharField(max_length=300, null=True, blank=True)
    title = models.CharField(max_length=300, null=True, blank=True)
    first_name = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return 'MySuperModel'

    def __check_field__(self):
        return self.name


class Pizza(models.Model):
    name = models.CharField(max_length=300)
    price = models.DecimalField(max_digits=9, decimal_places=2)

    def __str__(self):
        return self.name

    def create_order(self, count):
        return InstancePizza.objects.create(
            name=self.name,
            price=self.price,
            pizza_template=self,
            count=count
        )


class InstancePizza(models.Model):
    name = models.CharField(max_length=300, null=True, blank=True)
    price = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True)
    count = models.PositiveIntegerField(default=1)
    pizza_template = models.ForeignKey(Pizza, related_name='pizza_template', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return 'name: {}, price: {}, full_price: {}'.format(self.name, str(self.price), str(self.price * self.count)) 

class Order(models.Model):
    pizzas = models.ManyToManyField(InstancePizza, null=True, blank=True)
    full_price = models.DecimalField(max_digits=9, decimal_places=2)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return 'Order: {}, price: {}'.format(self.id, str(self.name)) 
