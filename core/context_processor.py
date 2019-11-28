# coding=utf-8
from django.conf import settings
from myAPP.models import Pizza, Order

def contex_core(request):
    if request.user.is_authenticated:
        order = Order.objects.filter(user=request.user).first()
    else:
        order = None
    return {'site_url': settings.SITE_URL,
            'site_name': settings.SITE_NAME,
            'order': order,
            'support_email_address': settings.SUPPORT_EMAIL_ADDRESS,}


# Создать новую модель - InstancePizza
# Добавить в Order связь MtM на InstancePizza
# Добавить возможность добавлять блюда в заказ
# Создать корзину, в которой можно редактировать блюда 
# Выводить итоговую сумму с учетом всех блюд в корзине
