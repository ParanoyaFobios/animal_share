from django.urls import path, re_path
from .views import PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView, AddCommentView, UserCommentListView, GalleryListView, Delete_Comment
from . import views

urlpatterns = [
    re_path(r'^user/(?P<username>\w{0,50})/$', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:pk>/comments', AddCommentView.as_view(), name='add_comment'),
    path('post/user_comments', UserCommentListView.as_view(), name='user-comments'),
    path('comment/delete/<int:comment_id>/', Delete_Comment, name='delete-comment'),
    path('post/gallery', GalleryListView.as_view(), name='gallery'),
    path('about/', views.about, name='blog-about'),
] 
