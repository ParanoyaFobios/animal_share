from django.db import models


class Categories(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=150, unique=True, blank=True, null=True, verbose_name = 'URL')

    class Meta:
        db_table = 'category' #переименование таблицы в БД из Categories в category
        verbose_name = 'Категорию' #альтернативное имя для отображения в админке
        verbose_name_plural = 'Категории' #тоже самое, но с указанием множественного числа

    def __str__(self) -> str:
        return self.name


class Products(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=150, unique=True, blank=True, null=True, verbose_name = 'URL')
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(default='default_animal.jpg', upload_to='catalog_pics')
    price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2)
    discount = models.DecimalField(default=0.00, max_digits=7, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(to=Categories, on_delete = models.CASCADE)


    class Meta:
        db_table = 'product'

    def __str__(self) -> str:
        return self.name #тут мы реализовали изменение названия товаров в админ панеле. Если без этой функции, категории и товары будут выглядеть как: Object_1 и т.д.
    
    def display_id(self):
        return f"{self.id:05}" #функция с помощью которой мы изменяем внешний вид айдишника товара, обычно он выглядит просто 1-2-3, тут мы ф-строкой меняем отображение на 00001, 00002..
    
    def sell_price(self):
        if self.discount:
            return round(self.price - self.discount*self.price/100, 2)
        return self.price #функция высчитывающая скидку