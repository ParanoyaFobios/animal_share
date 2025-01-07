from django.shortcuts import render
from goods.models import Products






def catalog(request): #контроллер отображения каталога находится в пользовательских тагах goods_tags.py
    goods = Products.objects.all().order_by('?')

    context = {
        'title':'Goods categories',
        'goods' : goods,
    }
    return render(request, 'goods/catalog.html', context,)

#Products.objects.filter(category__id=9).order_by('-price') сортировка обьектов бд по категории Cat's gear, сначала дешевые, потом дорогие

def product(request, product_slug):
    product = Products.objects.get(slug=product_slug) #в блоге и комментах я настраивал контроллер по айдишнику, но для товаров в магазине предпочтительней в аргумент урл диспатчера передавать слаг, облегчает работу поисковикам
    context = {
        'product' : product
        }
    return render(request, 'goods/product.html', context,)


