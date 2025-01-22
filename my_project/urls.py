"""
URL configuration for my_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from my_app.views import my_my_app
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('my_app/', my_my_app, name='my_app'),
    path('', views.home, name='home'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('whyclingcanhelp/', views.whyclingcanhelp, name='whyclingcanhelp'),
    path('servicesavailable/', views.servicesavailable, name='servicesavailable'),
    path('helpus/', views.helpus, name='helpus'),
    path('community/', views.community, name='community'),
    path('contactus/', views.contactus, name='contactus'),
    path('loginregister/', views.loginregister, name='loginregister'),
]
