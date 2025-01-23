from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('whyclingcanhelp/', views.whyclingcanhelp, name='whyclingcanhelp'),
    path('servicesavailable/', views.servicesavailable, name='servicesavailable'),
    path('helpus/', views.helpus, name='helpus'),
    path('community/', views.community, name='community'),
    path('community/posts/', views.post_list, name='post_list'),
    path('contactus/', views.contactus, name='contactus'),
    path('loginregister/', views.loginregister, name='loginregister'),
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('profiles/', views.profile_list, name='profile_list'),
]