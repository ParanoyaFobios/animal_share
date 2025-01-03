from django.urls import path
from .views import usertouserCreateView, usertouserListView, usertouserDetailListView, usertouserOutboxListView
app_name = 'usertouser' #указание для пространства имен в главном файле url.py


urlpatterns = [
path('sms/inbox/', usertouserListView.as_view(template_name='messages/inbox.html'), name='inbox'),
path('sms/create/<str:recipient>/', usertouserCreateView.as_view(), name='create_message'),
path('sms/outbox/', usertouserOutboxListView.as_view(template_name='messages/outbox.html'), name='outbox'),
path('sms/<int:pk>/', usertouserDetailListView.as_view(), name='detail'), 
]