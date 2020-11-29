from django.shortcuts import render, reverse
from django.views.generic import ListView, CreateView
from django.contrib.messages.views import SuccessMessageMixin, messages

from .models import Address, UserMessage

from .forms import UserMessageCreationForm


class ContactView(SuccessMessageMixin, CreateView):
    form_class = UserMessageCreationForm
    template_name = 'contact/contact_view.html'
    success_message = "Thank you for your complement :)"

    def get_context_data(self, *args, **kwargs):
        context = super(ContactView, self).get_context_data(*args, **kwargs)
        context['contact_context'] = Address.objects.all()[:1]
        context['title'] = 'Contact'
        return context

    def form_valid(self, form):
        instance = form.save(commit=True)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('contact')
