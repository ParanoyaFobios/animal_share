from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.db import transaction
from django.forms import ValidationError
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import FormView
from django.core.exceptions import ValidationError
from carts.models import Carts

from orders.forms import CreateOrderForm
from orders.models import Order, OrderItem



@login_required
def create_order(request):
    if request.method == 'POST':#если пост запрос, мы создаем форму при условии ее валидности
        form = CreateOrderForm(data=request.POST)
        if form.is_valid():
            try:
                with transaction.atomic():#атомарные транзакции - при одном запросе, выполняют множество действий и запросов с БД
                    user = request.user#команда одна - действий много, уменьшение количества товара, создание новой таблицы с записями и тд
                    cart_items = Carts.objects.filter(user=user)#получаю все корзины текущего пользователя

                    if cart_items.exists():#если все запросы и изменения произойдут без ошибок, коммит произойдет в бд, если что то из перечисленного ниже не пройдет валидацию, коммита не будет и нагрузки на бд тоже
                        # Создать заказ
                        order = Order.objects.create(
                            user=user,
                            phone_number=form.cleaned_data['phone_number'],
                            requires_delivery=form.cleaned_data['requires_delivery'],
                            delivery_address=form.cleaned_data['delivery_address'],
                            payment_on_get=form.cleaned_data['payment_on_get'],
                        )#
                        # Создать заказанные товары
                        for cart_item in cart_items:
                            product=cart_item.product
                            if not product:
                                raise ValidationError(f'Product not found in cart item {cart_item.id}')
                            name=cart_item.product.name
                            price=cart_item.product.sell_price()
                            quantity=cart_item.quantity


                            if product.quantity < quantity:
                                raise ValidationError(f'Not enoth {name} in facility\
                                                       Aviable {product.quantity} pieces')

                            OrderItem.objects.create(
                                order=order,
                                product=product,
                                name=name,
                                price=price,
                                quantity=quantity,
                            )
                            product.quantity -= quantity
                            product.save()#одна из транзакций, изменение количества товара в наличии

                        # Очистить корзину пользователя после создания заказа
                        cart_items.delete()

                        messages.success(request, 'Ordered!')
                        return redirect('profile')
            except ValidationError as e:#если трай не срабатывает, включается это условие
                messages.error(request, str(e))
                return redirect('create_order')
    else:#до пост запроса, подставляем существующие данные в форму 
        initial = {
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            'phone_number': request.user.profile.phone_number if hasattr(request.user, 'profile') else '',  # Проверка наличия профиля
        }

        form = CreateOrderForm(initial=initial)



        form = CreateOrderForm(initial=initial)

    context = {
        'form': form,
        'order': True,
        'title':'Order creation',
    }
    return render(request, 'orders/create_order.html', context=context)
