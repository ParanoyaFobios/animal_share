from django.urls import path
from carts import views


urlpatterns = [
    path('users-cart/', views.users_cart, name='users-cart'),
    path('cart_add/<slug:product_slug>/', views.cart_add, name='cart-add'),
    path('cart_change/<slug:product_slug>/', views.cart_change, name='cart-change'),
    path('cart_remove/<slug:product_slug>', views.cart_remove, name='cart-remove'), #задействуем URL dispatcher см документацию джанго
    ]