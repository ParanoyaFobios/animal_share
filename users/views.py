from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid(): #если форма соответсвует всем правилам заполнения
            form.save() #сохраняем введеные данные в базу данных
            user = form.instance #получаем пользователя из поля заполненной формы
            auth.login(request, user) #логиним пользователя на сайт
            username = form.cleaned_data.get('username') #берем данные из формы с очисткой кеша и передаем в ф строку для приветствия
            messages.success(request, f'Account created for {username}!Enjoy!')
            return redirect('blog-home') #условие для отображения сообщения о успехе и перенаправления на главную страницу 
        elif form.is_valid() == False:
            form = UserRegisterForm()
            messages.error(request, 'Error during registration.')
            return render(request, 'users/register.html', {'form': form}) #альтернативное сообщение в случае ошибки регистрации 
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required #это декоратор связанный с настройкой animalshare/settings.py LOGIN_URL = 'login'
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Account has been updated!You may continue!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)