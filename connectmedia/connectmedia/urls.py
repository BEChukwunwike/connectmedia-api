"""
URL configuration for connectmedia project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import home_view, logout_view

urlpatterns = [
    path("", home_view, name='home'),
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("dj-rest-auth/logout/", logout_view, name="rest_logout"),
    path("dj_rest_auth/", include("dj_rest_auth.urls")),
    path("dj_rest_auth/registration/", include("dj_rest_auth.registration.urls")),
    path("", include("profiles.urls")),
    path("", include("posts.urls")),
    path("", include("comments.urls")),
    path("", include("likes.urls")),
    path("", include("followers.urls")),
    ]
