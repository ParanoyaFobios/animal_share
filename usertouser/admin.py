from django.contrib import admin
from .models import usertouser

class UserMessages(admin.ModelAdmin):
    list_display = ('sender', 'recipient', 'timestamp',)#реализовали отображение полей в админ панеле, не трогая models.py

admin.site.register(usertouser, UserMessages)
# Register your models here.
