from django import template
from carts.models import Carts


register = template.Library()


@register.simple_tag()
def user_carts(request):#беру обьект пользователя для поиска и отображения всех привязанных к нему корзин
    if request.user.is_authenticated:#только для авторизованных пользователей
        return Carts.objects.filter(user=request.user)