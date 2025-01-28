from django.contrib import admin
from .models import Carts


class CartsTabAdmin(admin.TabularInline):#настройка отображения товаров связанных с пользователем
    model = Carts#модель к которой идет привязка
    fields = 'product', 'quantity', 'created_timestamp'
    search_fields = 'product', 'quantity', 'created_timestamp'
    readonly_fields = ('created_timestamp',)
    extra = 1#доп поле для добавления пользователю нового заказа
    fk_name = 'profile' #поле для связи

@admin.register(Carts)
class UserCarts(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity', 'created_timestamp')
    list_filter = ['created_timestamp', 'user', 'product',]

