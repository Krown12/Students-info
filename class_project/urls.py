"""
URL configuration for class_project project.

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
from django.conf.urls import include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include
from todo.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("index/",index),
    path("",home),
    path("register-id/",register),
    path("blog/",blog),
    path("about-us/",aboutus),
    path('contact-us',contactus),
    path('students-info/',students_info),
    path('students_info/marked/<pk>/',marked),
    path('students_info/edit/<pk>/',edit),
    path('students_info/delete/<pk>/',delete),
    
]+ static(settings.MEDIA_URL,document_root =settings.MEDIA_ROOT)



