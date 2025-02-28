from django.shortcuts import render
from goods.models import Products
from django.core.paginator import Paginator
from goods.utils import q_search
from carts.models import Carts
from django.db.models import Sum #импорт функции подсчета суммы обьектов по полю quantity



def catalog(request, category_slug): #контроллер отображения каталога находится в пользовательских тагах goods_tags.py
    goods = Products.objects.filter(category__slug=category_slug)
    on_sale = request.GET.get('on_sale', None)
    order_by = request.GET.get('order_by', None)

    if on_sale:
        goods = goods.filter(discount__gt=0) #discount__gt означает условие greater then, lt - lesser then
    if order_by and order_by != 'default':
        goods = goods.order_by(order_by)

    context = {
        'title':'Animal products',
        'goods' : goods,
    }
    return render(request, 'goods/catalog.html', context, )


def catalog_all(request): #контроллер отображения каталога находится в пользовательских тагах goods_tags.py
    total_quantity = 0  # Инициализация переменной total_quantity
    if request.user.is_authenticated:
        user = request.user#получаю обьект пользовтеля, что бы в дальнейшем использовать его для отображения количества корзин
        total_quantity = Carts.objects.filter(user=user).aggregate(total_quantity=Sum('quantity'))['total_quantity']  # Получаем общее количество товаров в корзине
    else:
        user = request.session.session_key#присваеваю анонимному пользователю сессионный ключ по которому буду к нему обращаться
        total_quantity = Carts.objects.filter(session_key=user).aggregate(total_quantity=Sum('quantity'))['total_quantity'] or 0 # Получаем общее количество товаров в корзине для анонимного пользователя


    on_sale = request.GET.get('on_sale', None)#сортировка см goods/catalog.html
    order_by = request.GET.get('order_by', None)
    query = request.GET.get('q', None)

    if query:
        goods = q_search(query)
    else:
        goods = Products.objects.all()


    if on_sale:
        goods = goods.filter(discount__gt=0) #discount__gt означает условие greater then, думаю есть такое же lt - lesser then
    if order_by and order_by != 'default':
        goods = goods.order_by(order_by)

    paginator = Paginator(goods, 6) #пагинация не для классов, как я делал раьше, а для функций отображения
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'total_quantity': total_quantity,
        'title':'Animal products',
        'page_obj': page_obj,
        'goods' : page_obj,
    }
    return render(request, 'goods/catalog.html', context,)
#Products.objects.filter(category__id=9).order_by('-price') сортировка обьектов бд по категории Cat's gear, сначала дешевые, потом дорогие

def product(request, product_slug):
    product = Products.objects.get(slug=product_slug) #в блоге и комментах я настраивал контроллер по айдишнику, но для товаров в магазине предпочтительней в аргумент урл диспатчера передавать слаг, облегчает работу поисковикам
    context = {
        'product' : product,
        'title':'About product',
        }
    return render(request, 'goods/product.html', context,)


