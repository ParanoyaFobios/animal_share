from django.contrib import admin
from .models import Categories, Products

@admin.register(Categories) #декорируем и передаем в аргумент модель категории
class CategoriesAdmin(admin.ModelAdmin): #тонкая настройка регистрации в админ панели, с автозаполнением поля урл
    prepopulated_fields = {'slug':('name',)}


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}