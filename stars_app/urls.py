from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('photos/<int:pk>', views.photo_details, name='photo_details'),


]