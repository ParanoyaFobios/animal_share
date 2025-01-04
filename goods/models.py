from django.db import models

class Categories(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=150, unique=True, blank=True, null=True, verbose_name = 'URL')

    class Meta:
        db_table = 'category' #переименование таблицы в БД из Categories в category
        verbose_name = 'Категорию' #альтернативное имя для отображения в админке
        verbose_name_plural = 'Категории' #тоже самое, но с указанием множественного числа


class Products(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=150, unique=True, blank=True, null=True, verbose_name = 'URL')
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(default='default.jpg', upload_to='catalog_pics')
    price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2)
    discount = models.DecimalField(default=0.00, max_digits=7, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(to=Categories, on_delete = models.SET_DEFAULT, default='Other')#при удалении категории, все товары, которые остались ней, будут перемещены в категорию other, а не удалены каскадно, вслед за категорией


    class Meta:
        db_table = 'product'