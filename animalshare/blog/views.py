from typing import Any
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.contrib.auth.models import User


def home(request):
    context = {
        'posts' : Post.objects.all()
    }
    return render(request, 'home.html', context, {'animal_image': context})



class PostListView(ListView):
    model = Post
    template_name = 'home.html' #<app>/<model>_<view_type>.html это шаблон по которому джанго будет отрисовывать наши посты
    context_object_name = 'posts' #показываем название что зацикливать
    ordering = ['-date_posted'] #даем запрос в БД на отображение постов в порядке добавления
    paginate_by = 5 # метод, который позволяет оставить 5 постов на одну страницу


class UserPostListView(ListView): #создание класса который отфильтрует посты пользователя
    model = Post
    template_name = 'user_posts.html' 
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'animaltype', 'animalstatus', 'description', 'animal_image']

    def form_valid(self, form):
        form.instance.author = self.request.user #присваиваем этой функцией текущего автора создаваемому посту
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'animaltype', 'animalstatus', 'description', 'animal_image']

    def form_valid(self, form):
        form.instance.author = self.request.user #присваиваем этой функцией текущего автора создаваемому посту
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False #функция которая позволяет редактировать только те посты, автором которых является пользователь
    

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def about(request):
    return render(request, 'about.html', {'title' : 'About'})






# Create your views here.
