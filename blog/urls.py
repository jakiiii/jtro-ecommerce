from django.urls import path
from .views import (
    BlogHomeView,
    BlogDetailView,
    BlogCategoryListView,
    BlogSearchListView
)

urlpatterns = [
    path('blog/', BlogHomeView.as_view(), name='blog-home'),
    path('blog/<slug:slug>/', BlogDetailView.as_view(), name='blog-post-detail'),
    path('blog/category/<slug:slug>/', BlogCategoryListView.as_view(), name='blog-category'),
    path('blog/jtro/search/', BlogSearchListView.as_view(), name='blog-search')
]
