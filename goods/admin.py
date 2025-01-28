from django.contrib import admin
from .models import Categories, Products

@admin.register(Categories) #декорируем и передаем в аргумент модель категории
class CategoriesAdmin(admin.ModelAdmin): 
    prepopulated_fields = {'slug':('name',)}#тонкая настройка регистрации в админ панели, с автозаполнением поля урл, создается поле слаг


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display = ['name', 'quantity', 'price', 'category', 'discount']
    list_editable = ['price', 'discount',]
    search_fields = ['name', 'description',]
    list_filter = ['discount', 'category', 'quantity']
    fields = [
        'name',
        'category',
        'slug',
        'description',
        'image',
        ('price', 'discount'),
        'quantity',
    ]#как будут отображаться ячейки при добавлении товара