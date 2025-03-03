from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from carts.models import Carts
from orders.models import Order, OrderItem
from django.db.models import Prefetch
from random import randint


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid(): #если форма соответсвует всем правилам заполнения
            form.save() #сохраняем введеные данные в базу данных
            session_key = request.session.session_key#получаю экземпляр кулюча сессии не зареганого пользователя
            user = form.instance #получаем пользователя из поля заполненной формы
            auth.login(request, user) #логиним пользователя на сайт
            if session_key:#если сессионный ключ есть, перекидываем его на пользователя
                Carts.objects.filter(session_key=session_key).update(user=user)#товары которые не хареганный пользователь забросил в корзину, после регистрации появятся в его заказах
            username = form.cleaned_data.get('username') #берем данные из формы с очисткой кеша и передаем в ф строку для приветствия
            messages.success(request, f'Account created for {username}!Enjoy!')
            return redirect('home') #условие для отображения сообщения о успехе и перенаправления на главную страницу 
        else:
            messages.error(request, 'Error during registration.')
            return render(request, 'users/register.html', {'form': form, 'title': 'Registration', 'variable': randint(1, 9),}) #альтернативное сообщение в случае ошибки регистрации 
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form, 'title': 'Registration', 'variable': randint(1, 9),})

@login_required #это декоратор связанный с настройкой animalshare/settings.py LOGIN_URL = 'login', дает доступ к контроллеру только авторизированным пользователям, выдаст 404 если не указать в настройках куда редиректить
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)#request.FiLES необходимо для того, что бы форма приняла файлы картинок
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Account has been updated! You may continue!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)#instance передает обьект пользователя, что б при изменении профиля пользователя, сразу отображались его текущие данные
        p_form = ProfileUpdateForm(instance=request.user.profile)

        orders = Order.objects.filter(user=request.user).prefetch_related(
                        Prefetch(
                            "orderitem_set",
                            queryset=OrderItem.objects.select_related("product"),
                        )
                    ).order_by("-id")
    context = {
        'variable': randint(1, 9),
        'u_form': u_form,
        'p_form': p_form,
        'orders': orders,
        'title': 'Profile and orders'
    }

    return render(request, 'users/profile.html', context)