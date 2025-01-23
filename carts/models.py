from django.db import models
from goods.models import Products
from django.contrib.auth.models import User

class CartQuerySet(models.QuerySet):

    def totall_price(self):#посчет суммы всех товаров во всех корзинах пользователя
        return sum(x.products_price() for x in self)#генератор, который берет метод products_price и проходится им по каждой корзине

    def totall_quantity(self):
        if self:
            return sum(x.quantity for x in self)
        return 0
    

class Carts(models.Model):#каждый товар в пользовательской корзине, даже не купленный, будет создавать свою отдельную карзину в бд для сбора статистики

    user = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=True, null=True, verbose_name='User')
    product = models.ForeignKey(to=Products, on_delete=models.CASCADE, verbose_name='Ordered goods')
    quantity = models.PositiveSmallIntegerField(default=0, verbose_name='Pieces')
    session_key = models.CharField(max_length=32, null=True, blank=True)
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Date added')

    objects = CartQuerySet().as_manager()#функция для подсчета корзин пользователя, создал отдельный класс

    class Meta:
        db_table = 'cart'
        verbose_name = 'Market busket'

    def products_price(self):#функция для посчета цены отдельно взятой позиции товара
        return round(self.product.sell_price() * self.quantity, 2)

    def __str__(self) -> str:#тображение в админке
        return f"{self.user.username}'s busket| Product {self.product.name}| Quantity {self.quantity}"
