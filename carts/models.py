from django.db import models
from users.models import Profile
from goods.models import Products

class Carts(models.Model):

    user = models.ForeignKey(to=Profile, on_delete=models.CASCADE, verbose_name='User')
    product = models.ForeignKey(to=Products, on_delete=models.CASCADE, verbose_name='Ordered good')
    quantity = models.PositiveSmallIntegerField(default=0, verbose_name='Pieces')
    created_timestamp = models.DateTimeField(auto_add_now=True, verbose_name='Date added')

    class Meta:
        verbose_name = 'Market busket'

    def __str__(self) -> str:
        return f'Buket of {self.user.user}| Product {self.product.name}| Quantity {self.quantity}'
