from django.db import models
from accounts.models import User
from django_resized import ResizedImageField


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
    image = ResizedImageField(size=[1280, 720], upload_to='pizzas/', null=True, blank=True)

    def __str__(self):
        return self.name

    def create_instance_pizza(self, count):
        return InstancePizza.objects.create(
            name=self.name,
            price=self.price,
            pizza_template=self,
            count=count
        )

    def change_price(self, price):
        self.price += price
        self.save()


class InstancePizza(models.Model):
    name = models.CharField(max_length=300, null=True, blank=True)
    price = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True)
    count = models.PositiveIntegerField(default=1)
    pizza_template = models.ForeignKey(Pizza, related_name='pizza_template', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return 'name: {}, price: {}, count: {}'.format(self.name, str(self.price), str(self.count)) 

class Order(models.Model):
    pizzas = models.ManyToManyField(InstancePizza, null=True, blank=True)
    full_price = models.DecimalField(max_digits=9, decimal_places=2)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return 'Order: {}, price: {}'.format(self.id, str(self.full_price)) 

    def get_full_price(self):
        pizzas = self.pizzas.all()
        full_price = 0
        for pizza in pizzas:
            full_price += pizza.price * pizza.count
        return full_price
