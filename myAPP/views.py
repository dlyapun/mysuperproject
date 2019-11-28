from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.views.generic import TemplateView, View
from django import forms
from myAPP.models import *

class PizzaForm(forms.Form):
    pizza_id = forms.IntegerField()
    count = forms.IntegerField()


class CoreTemplateView(TemplateView):
    template_name = 'list.html'
    sorting_fields = ['price', 'name', '-price', '-name']

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.method == 'POST':
            ordering = self.request.POST.get('ordering', 'name')
        if self.request.method == 'GET':
            ordering = self.request.GET.get('ordering', 'name')    
        if ordering not in self.sorting_fields:
            ordering = 'name'
        context['pizzas'] = Pizza.objects.all().order_by(ordering)
        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return render(request, self.template_name, context)

class CartView(TemplateView):
    template_name = 'cart.html'

class AddPizzaView(FormView):
    template_name = 'contact.html'
    form_class = PizzaForm
    success_url = '/pizzas/'

    def form_valid(self, form):
        print('form.cleaned_data:', form.cleaned_data)
        pizza = Pizza.objects.get(id=form.cleaned_data.get('pizza_id'))
        count = form.cleaned_data.get('count')
        instance_pizza = pizza.create_instance_pizza(count)
        order, created = Order.objects.get_or_create(user=self.request.user, full_price=0)
        order.pizzas.add(instance_pizza)
        return super().form_valid(form)

class DeletePizzaView(View):

    def post(self, request, *args, **kwargs):
        InstancePizza.objects.filter(id=request.POST.get('pizza_id')).delete()
        return redirect('/cart/')
