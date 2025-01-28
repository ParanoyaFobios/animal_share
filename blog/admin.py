from django.contrib import admin
from .models import Post, Comment

@admin.register(Post)
class UserPosts(admin.ModelAdmin):
    list_display = ['author', 'title', 'animaltype', 'animalstatus', 'date_posted']


@admin.register(Comment)
class UserComments(admin.ModelAdmin):
    list_display = ['comment_author', 'post', 'date_added',]
    list_filter = ['comment_author', 'post', 'date_added',]

# admin.site.register(Post, UserPosts)
# admin.site.register(Comment)

