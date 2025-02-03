from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class usertouser(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    subject = models.CharField(max_length=255)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    
    # def __str__(self):
    #     return self.subject
    #нюанс в том, что сюда, можно писать только Charfield и TextField, если будут числа или айди вылазит ошибка
    #леко меняется в admin.py

    def get_absolute_url(self):
        return reverse('inbox')