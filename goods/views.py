from django.shortcuts import render
from goods.models import Products, Categories




def catalog(request):
    categories = Categories.objects.all()
    goods = Products.objects.all()
    context = {
        'title':'Goods categories',
        'categories': categories,
        'goods' : goods,
    }
    return render(request, 'goods/catalog.html', context,)

#Products.objects.filter(category__id=9).order_by('-price') сортировка обьектов бд по категории Cat's gear, сначала дешевые, потом дорогие

def product(request):
    return render(request, 'goods/product.html', context)

