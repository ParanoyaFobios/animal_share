from django.urls import path
from orders import views


urlpatterns = [
    path('create_order/', views.create_order, name='create-order'),
]