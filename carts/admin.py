from django.contrib import admin
from .models import Carts


class UserCarts(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity', 'created_timestamp')


admin.site.register(Carts, UserCarts)