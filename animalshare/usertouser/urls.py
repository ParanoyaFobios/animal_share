from django.urls import path
from .views import usertouserCreateView, usertouserListView, usertouserDetailListView



urlpatterns = [
path('sms/inbox/', usertouserListView.as_view(template_name='messages/inbox.html'), name='inbox'),
path('sms/create/', usertouserCreateView.as_view(), name='create_message'),
path('sms/outbox/', usertouserListView.as_view(template_name='messages/outbox.html'), name='outbox'),
path('sms/<int:pk>/', usertouserDetailListView.as_view(), name='detail'),
]