from django.views.generic import CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from .models import usertouser


class usertouserCreateView(LoginRequiredMixin, CreateView):
    model = usertouser
    fields = ['recipient', 'subject', 'content']
    template_name = 'messages/create.html'
    context_object_name = 'create_message'
    success_url = ('/')

    def form_valid(self, form):
        form.instance.sender = self.request.user
        return super().form_valid(form)

class usertouserListView(LoginRequiredMixin, ListView):
    model = usertouser
    template_name = 'messages/inbox.html'
    context_object_name = 'sms'
    ordering = ['-timestamp']

    def get_queryset(self):
        return usertouser.objects.filter(recipient=self.request.user)