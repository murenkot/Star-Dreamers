from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.main_page, name='main_page'),
    path('photos/<int:pk>', views.photo_details, name='photo_details'),
    path('photos/<int:pk>/comments/add', views.add_comment, name='add_comment'),
    
]