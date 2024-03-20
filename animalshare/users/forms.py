from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm): #в агрументе класса указано откуда он унаследован, вся эта лабуда сделана для того что б добавить строку мыла в стандартную регистрационную форму
    email = forms.EmailField()

    class Meta: #что мы хотим видеть в моделе нашей формы регистрации
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta: #что мы хотим видеть в моделе нашей формы регистрации
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']