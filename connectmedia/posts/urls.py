"""This module defines the URL patterns for the posts app."""
from django.urls import path
from posts import views


# Define the URL patterns for the posts app.
urlpatterns = [
    path('posts/', views.PostList.as_view()),
    path('posts/<int:pk>', views.PostDetail.as_view()),
]
