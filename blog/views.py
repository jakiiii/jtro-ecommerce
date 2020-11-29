from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

from .models import BlogPost, BlogCategory


class BlogHomeView(ListView):
    paginate_by = 10
    model = BlogPost
    template_name = 'blog/blog_home.html'
    context_object_name = 'blog_content'

    def get_context_data(self, *args, **kwargs):
        context = super(BlogHomeView, self).get_context_data(*args, **kwargs)
        context['blog_category_context'] = BlogPost.objects.all().distinct()
        context['title'] = 'Blog'
        return context


class BlogDetailView(DetailView):
    model = BlogPost
    template_name = 'blog/blog_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(BlogDetailView, self).get_context_data(*args, **kwargs)
        context['title'] = '{}'.format(self.get_object().title)
        context['blog_category_context'] = BlogPost.objects.all()  # .distinct('category')
        return context


class BlogCategoryListView(ListView):
    template_name = 'blog/blog_home.html'
    context_object_name = 'blog_content'

    def get_queryset(self, *args, **kwargs):
        category_slug = self.kwargs.get('slug', None)
        if category_slug:
            return BlogPost.objects.filter(category_name__blog_category_name__iexact=category_slug)
            # return BlogCategory.objects.category_name(category_slug)

    def get_context_data(self, *args, **kwargs):
        context = super(BlogCategoryListView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Category View'
        context['blog_category_context'] = BlogPost.objects.all()  # .distinct('category')
        return context


class BlogSearchListView(ListView):
    model = BlogPost
    template_name = 'blog/blog_home.html'
    context_object_name = 'blog_content'

    def get_queryset(self):
        query = self.request.GET.get('q', None)
        if query is not None:
            return BlogPost.objects.search(query)
        else:
            return BlogPost.objects.none()

    def get_context_data(self, *args, **kwargs):
        context = super(BlogSearchListView, self).get_context_data(*args, **kwargs)
        context['title'] = self.request.GET.get('q')
        context['blog_category_context'] = BlogPost.objects.all()  # .distinct('category')
        return context
