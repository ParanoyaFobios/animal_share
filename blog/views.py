from typing import Any
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Comment
from django.contrib.auth.models import User



def home(request):
    context = {
        'posts' : Post.objects.all(),
        'comments' : Comment.objects.all(),
        'gallery' : Post.objects.all(),
    }
    return render(request, 'home.html', 'user_comments.html', 'gallery.html', context, {'animal_image': context}, {'comments':context}, {'gallery': context},)


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
    ordering = ['-date_posted']

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')



class GalleryListView(ListView): #создание класса который отфильтрует из БД все картинки
    model = Post
    template_name = 'gallery.html' 
    context_object_name = 'gallery'
    paginate_by = 18
    ordering = ['?']
    # def get_queryset(self):
    #     return Post.objects.values_list('animal_image', flat=True)


class UserCommentListView(ListView): #создание класса который отфильтрует комментарии пользователя
    model = Comment
    template_name = 'user_comments.html' 
    context_object_name = 'comments'
    paginate_by = 20
    ordering = ['-date_added']

    def get_queryset(self):
        user = get_object_or_404(User, id=self.request.user.id)
        return Comment.objects.filter(comment_author=user).order_by('-date_added')



class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'animaltype', 'animalstatus', 'description', 'animal_image']

    def form_valid(self, form):
        form.instance.author = self.request.user #присваиваем этой функцией текущего автора создаваемому посту
        return super().form_valid(form)


class AddCommentView(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ['body', ]
    template_name = 'new_comment.html' #<app>/<model>_<view_type>.html это шаблон по которому джанго будет отрисовывать наши посты
    context_object_name = 'comments'
    # #даем запрос в БД на отображение постов в порядке добавления
    #paginate_by = 5

    def form_valid(self, form):
        form.instance.comment_author = self.request.user #присвоили коменту текущего пользователя
        form.instance.post_id = self.kwargs['pk'] #присвоили коменту айди текущего поста
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


class PostDetailView(DetailView):
    model = Post


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
