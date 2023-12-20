"""This module defines the URL patterns for the profiles app."""
from django.urls import path
from profiles import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('profiles/', views.ProfileList.as_view()),
    path('profiles/<int:pk>', views.ProfileDetail.as_view()),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
