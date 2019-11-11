from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('profile/create/', views.profile_create, name="profile_create"),
    path('profile/author/<int:pk>', views.profile_show, name='profile_show'),
    
]