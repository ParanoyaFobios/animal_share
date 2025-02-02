from django.shortcuts import render, redirect
from goods.models import Products
from carts.models import Carts
from django.http import JsonResponse



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
    else:
        carts = Carts.objects.filter(session_key=request.session.session_key, product=product)
        if carts.exists():
            cart = carts.first()
            if cart:
                cart.quantity += 1
                cart.save()
        else:
            Carts.objects.create(session_key=request.session.session_key, product=product, quantity = 1)
    return redirect(request.META['HTTP_REFERER'])#эта команда возвращает пользователя на страницу с которой он сюда попал

    
def cart_change(request, product_slug):
    if request.method == 'POST':
        action = request.POST.get('action')
        cart_id = request.POST.get('cart_id')
        cart = Carts.objects.get(id=cart_id)

        if action == 'increase':
            cart.quantity += 1
        elif action == 'decrease' and cart.quantity > 1:
            cart.quantity -= 1
        
        cart.save()

        # Получаем обновленные значения для всех товаров в корзине
        if request.user.is_authenticated:
            total_quantity = Carts.objects.filter(user=request.user).totall_quantity()
            total_price = Carts.objects.filter(user=request.user).totall_price()
        else:
            total_quantity = Carts.objects.filter(session_key=request.session.session_key).totall_quantity()
            total_price = Carts.objects.filter(session_key=request.session.session_key).totall_price()

        return JsonResponse({
            'new_quantity': cart.quantity,
            'total_quantity': total_quantity,
            'total_price': total_price,
            'title': 'Animalshop',
        })


    
    
def cart_remove(request, cart_id):
    if request.method == 'POST':
        cart = Carts.objects.get(id=cart_id)
        cart.delete()

        # Получаем обновленные значения для всех товаров в корзине
        if request.user.is_authenticated:
            total_quantity = Carts.objects.filter(user=request.user).totall_quantity()
            total_price = Carts.objects.filter(user=request.user).totall_price()
        else:
            total_quantity = Carts.objects.filter(session_key=request.session.session_key).totall_quantity()
            total_price = Carts.objects.filter(session_key=request.session.session_key).totall_price()

        return JsonResponse({
            'success': True,
            'total_quantity': total_quantity,
            'total_price': total_price,
            'title': 'Animalshop',
        })

    
