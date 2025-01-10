from django import template
from goods.models import Categories
from django.utils.http import urlencode

register = template.Library()


@register.simple_tag() #декоратор для работы с функцией отфильтровывания категорий, что б не создавать каждый контроллер отдельно для каждой категории товара
def tag_categories():
    return Categories.objects.all().order_by('name') #работает в обход контроллеров из views.py

@register.simple_tag(takes_context=True)
def change_params(context, **kwargs):
    query = context['request'].GET.dict()
    query.update(kwargs)
    return urlencode(query)