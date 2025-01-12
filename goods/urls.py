from django.urls import path
from goods import views



urlpatterns = [
    path('search/', views.catalog_all, name='search'),
    path('', views.catalog_all, name='catalog-all'),
    path('<slug:category_slug>/', views.catalog, name='catalog'),
    path('product/<slug:product_slug>/', views.product, name='product'), #задействуем URL dispatcher см документацию джанго
    ]