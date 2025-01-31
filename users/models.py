from django.db import models
from django.contrib.auth.models import User
#from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) #
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    phone_number = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return f'{self.user.username} Profile' #переопределение надписи в админке, вместо object(1), будет отобржаться юзернейм профиль
    

    #def save(self, *args, **kwargs):
    #    super(Profile,self).save(*args, **kwargs)
    
    #    img = Image.open(self.image.path) #открываем изображение с помощью подушки
    #    if img.height > 800 or img.width > 800:#условие для сверки размера
    #       output_size = (800, 800)#команда конвертации
    #       img.thumbnail(output_size)#продолжение команды конвертации
    #       img.save(self.image.path)#сохранение с перезаписью, путь перезаписи в аргументе
