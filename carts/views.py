from django.shortcuts import render, redirect
from goods.models import Products
from carts.models import Carts


def users_cart(request):
    return render(request, 'carts/users_cart.html')


def cart_add(request, product_slug):
    product = Products.objects.get(slug=product_slug)#получем экземпляр продукта

    if request.user.is_authenticated:
        carts = Carts.objects.filter(user=request.user, product=product)#фильтруем по ползователю и конкретному продукту
        if carts.exists():#если продукт уже в корзине, увеличиваем его количество на 1
            cart = carts.first()
            if cart:
                cart.quantity += 1
                cart.save()
        else:
            Carts.objects.create(user=request.user, product=product, quantity = 1)#если продукта нет в корзине, создаем этот обьект
    return redirect(request.META['HTTP_REFERER'])#эта команда возвращает пользователя на страницу с которой он сюда попал

    
def cart_change(request, product_slug):
    ...
def cart_remove(request, product_slug):
    ...