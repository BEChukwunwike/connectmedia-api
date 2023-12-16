"""This module defines the URL patterns for the posts app."""
from django.urls import path
from posts import views
from .views import PostDetail

urlpatterns = [
    path('posts/', views.PostList.as_view()),
    path('posts/<int:pk>', views.PostDetail.as_view()),
]