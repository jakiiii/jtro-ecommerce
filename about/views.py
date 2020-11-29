from django.shortcuts import render

from django.views.generic import TemplateView


class AboutView(TemplateView):
    template_name = 'about/about.html'

    def get_context_data(self, *args, **kwargs):
        context = super(AboutView, self).get_context_data(*args, **kwargs)
        context['title'] = 'About'
        return context
