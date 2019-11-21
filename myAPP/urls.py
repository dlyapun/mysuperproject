# coding=utf-8

from .views import *
from django.conf.urls import url, include
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^pizzas/$', CoreTemplateView.as_view()),
    url(r'^add_pizza/$', AddPizzaView.as_view()),
]