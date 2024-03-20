from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    animaltype = models.CharField(max_length=50)
    animalstatus = models.CharField(max_length=50, null=True)
    description = models.TextField()
    animal_image = models.ImageField(default='default_animal.jpg', upload_to='animal_pics')
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk}) #перенаправление после создания поста в детали поста