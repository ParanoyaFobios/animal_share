from django.urls import path, re_path
from .views import usertouserCreateView, usertouserListView



urlpatterns = [
path('inbox/', usertouserListView.as_view(template_name='messages/inbox.html'), name='inbox'),
path('create/', usertouserCreateView.as_view(template_name='messages/create.html'), name='create_message'),
path('outbox/', usertouserListView.as_view(template_name='messages/outbox.html'), name='outbox'),
path('deleted/', usertouserListView.as_view(template_name='messages/deleted.html'), name='deleted'),
]