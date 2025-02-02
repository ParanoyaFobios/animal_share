from django.views.generic import CreateView, ListView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.utils.functional import lazy
from django.urls import reverse
from .models import usertouser
from django.contrib.auth.models import User


class usertouserCreateView(LoginRequiredMixin, CreateView):
    model = usertouser
    fields = ['subject', 'content']
    template_name = 'messages/create.html'
    context_object_name = 'create_message'
    success_url = lazy(reverse, str)('outbox')

    def get_initial(self):
        initial = super(usertouserCreateView, self).get_initial()
        initial['recipient'] = User.objects.get(username=self.kwargs['recipient'])
        return initial

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        recipient = self.kwargs.get('recipient')  # Получаем получателя из URL параметра
        context['recipient'] = recipient
        context['title'] = 'Create message'
        return context

    def form_valid(self, form):
        form.instance.sender = self.request.user
        recipient_username = self.kwargs['recipient']
        recipient = User.objects.get(username=recipient_username)  # Получаем экземпляр пользователя по имени
        form.instance.recipient = recipient  # Устанавливаем получателя из найденного пользователя
        return super().form_valid(form)
    


class usertouserListView(LoginRequiredMixin, ListView):
    model = usertouser
    template_name = 'messages/inbox.html'
    context_object_name = 'sms'
    paginate_by = None


    def get_queryset(self):
        return usertouser.objects.filter(recipient=self.request.user).order_by('-timestamp')
    

    

class usertouserOutboxListView(LoginRequiredMixin, ListView):
    model = usertouser
    template_name = 'messages/outbox.html'
    context_object_name = 'sms'
    paginate_by = None


    def get_queryset(self):
        return usertouser.objects.filter(sender=self.request.user).order_by('-timestamp')
    
    

class usertouserDetailListView(DetailView, LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = usertouser
    template_name = 'messages/detail.html'
    success_url = lazy(reverse, str)('inbox')
    
    def test_func(self):
        sms = self.get_object()
        if self.request.user == sms.recipient:
            return True
        return False