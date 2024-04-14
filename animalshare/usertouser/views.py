from django.views.generic import CreateView, ListView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.utils.functional import lazy
from django.urls import reverse
from .models import usertouser
from blog.models import Post


class usertouserCreateView(LoginRequiredMixin, CreateView, Post):
    model = usertouser
    fields = ['recipient', 'subject', 'content']
    template_name = 'messages/create.html'
    context_object_name = 'create_message'


    def form_valid(self, form):
        form.instance.sender = self.request.user
        #form.instance.recipient = Post.request.author
        return super().form_valid(form)

class usertouserListView(LoginRequiredMixin, ListView):
    model = usertouser
    template_name = 'messages/inbox.html'
    context_object_name = 'sms'
    ordering = ['-timestamp']
    paginate_by = 20


    def get_queryset(self):
        return usertouser.objects.filter(recipient=self.request.user)
    

    

class usertouserOutboxListView(LoginRequiredMixin, ListView):
    model = usertouser
    template_name = 'messages/outbox.html'
    context_object_name = 'sms'
    ordering = ['-timestamp']
    #paginate_by = 20

    def get_queryset(self):
        return usertouser.objects.filter(sender=self.request.user)
    

class usertouserDetailListView(DetailView, LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = usertouser
    template_name = 'messages/detail.html'
    success_url = lazy(reverse, str)('inbox')
    
    def test_func(self):
        sms = self.get_object()
        if self.request.user == sms.recipient:
            return True
        return False