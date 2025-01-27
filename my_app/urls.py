from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('whycyclingcanhelp/', views.whycyclingcanhelp, name='whycyclingcanhelp'),
    path('servicesavailable/', views.servicesavailable, name='servicesavailable'),
    path('helpus/', views.helpus, name='helpus'),
    path('community/', views.community, name='community'),
    path('community/posts/', views.post_list, name='post_list'),
    path('contactus/', views.contactus, name='contactus'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('profiles/', views.profile_list, name='profile_list'),
    path('profiles/<str:username>/', views.profile_detail, name='profile_detail'),
    path('profiles/<str:username>/follow/', views.follow_user, name='follow_user'),
    path('profiles/<str:username>/unfollow/', views.unfollow_user, name='unfollow_user'),
    path('create_post/', views.create_post, name='create_post'),
    path('edit_post/<int:post_id>/', views.edit_post, name='edit_post'),
    path('delete_post/<int:post_id>/', views.delete_post, name='delete_post'),
    path('posts/', views.post_list, name='post_list'),
    path('profile/<int:user_id>/', views.profile, name='profile'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('profile/edit/', views.profile_edit, name='profile_edit'),
    path('profile/delete/', views.delete_profile, name='delete_profile'),
]