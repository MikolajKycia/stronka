"""
URL configuration for twwb_backend project.

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
from django.urls import path
from pages.views import home_view, gallery_view, about_view, new_comment_view, contact_view
from comments.views import forum_view

urlpatterns = [
    path("", home_view, name="home"),
    path("home/", home_view, name="home"),
    path("gallery/", gallery_view, name = "gallery"),
    path("forum/", forum_view, name = "forum"),
    path("about/", about_view, name = "about"),
    path('new_comment/', new_comment_view, name='new_comment'),
    path("contact/", contact_view, name = 'contact'), 
    path("admin/", admin.site.urls),

]
