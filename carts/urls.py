from django.urls import path
from carts import views


urlpatterns = [
    path('users-cart/', views.users_cart, name='users-cart'),
    path('cart_add/<int:product_id>/', views.cart_add, name='cart-add'),
    path('cart_change/<int:product_id>/', views.cart_change, name='cart-change'),
    path('cart_remove/', views.cart_remove, name='cart-remove'), #задействуем URL dispatcher см документацию джанго
    ]