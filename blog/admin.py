from django.contrib import admin
from .models import Post, Comment


class UserPosts(admin.ModelAdmin):
    list_display = ('author', 'title', 'animaltype', 'animalstatus')
# class UserComments(admin.ModelAdmin):
#     list_display = ('comment_author', 'post', 'date_added',)

admin.site.register(Post, UserPosts)
admin.site.register(Comment)

