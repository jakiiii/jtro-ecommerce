from django.urls import path
from .views import (
    BlogHomeView,
)

urlpatterns = [
    path('blog/', BlogHomeView.as_view(), name='blog-home'),
]
