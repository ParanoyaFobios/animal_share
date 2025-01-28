from django.contrib import admin
from users.models import Profile
from carts.admin import CartsTabAdmin


# admin.site.register(Profile) #не забыть зарегестрировать новую модель в админке приложения
# @admin.register(Profile)
# class UserAdmin(admin.ModelAdmin):
#     list_display = ['user']
#     inlines = [CartsTabAdmin,]