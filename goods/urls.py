from django.urls import path
from goods import views



urlpatterns = [
    path('', views.catalog, name='catalog'),
    path('product/<slug:product_slug>/', views.product, name='product'), #задействуем URL dispatcher см документацию джанго
    ]