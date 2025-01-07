from django import template
from goods.models import Categories

register = template.Library()


@register.simple_tag() #декоратор для работы с функцией отфильтровывания категорий, что б не создавать каждый контроллер отдельно для каждой категории товара
def tag_categories():
    return Categories.objects.all().order_by('name') #работает в обход контроллеров из views.py