from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from .models import BlogPost


class BlogHomeView(ListView):
    paginate_by = 10
    model = BlogPost
    template_name = 'blog/blog_home.html'
    context_object_name = 'blog_content'

    def get_context_data(self, *args, **kwargs):
        context = super(BlogHomeView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Blog'
        return context
