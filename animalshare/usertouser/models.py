from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class usertouser(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    subject = models.CharField(max_length=255)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)


    def get_absolute_url(self):
        return reverse('inbox')