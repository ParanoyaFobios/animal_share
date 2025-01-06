from django.shortcuts import render
from goods.models import Products, Categories
from django.views.generic import ListView, DetailView




def catalog(request):
    goods = Products.objects.all().order_by('?')
    context = {
        'title':'Goods categories',
        'goods' : goods,
    }
    return render(request, 'goods/catalog.html', context,)

#Products.objects.filter(category__id=9).order_by('-price') сортировка обьектов бд по категории Cat's gear, сначала дешевые, потом дорогие

def product(request):
    return render(request, 'goods/product.html',)


