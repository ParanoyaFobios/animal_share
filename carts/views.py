from django.shortcuts import render


def users_cart(request):
    return render(request, 'carts/users_cart.html')


def cart_add(request, product_id):
    ...
def cart_change(request, product_id):
    ...
def cart_remove(request, product_id):
    ...