from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.main_page, name='main_page'),
    path('photos/<int:pk>', views.photo_details, name='photo_details'),
    path('photos/<int:pk>/like', views.add_like, name='add_like'),
    path('photos/<int:pk>/comments/add', views.add_comment, name='add_comment'),
    path('photos/<int:pk>/comments/edit/<int:comment_pk>', views.edit_comment, name='edit_comment'),
    path('photos/<int:pk>/comments/delete/<int:comment_pk>', views.delete_comment, name='delete_comment'),
    path('photos/<int:pk>/post/create', views.create_post, name='create_post'),
    path('posts/<int:pk>', views.post_details, name='post_details'),
    path('posts/<int:pk>/edit', views.post_edit, name='post_edit'),
    path('posts/<int:pk>/delete', views.post_delete, name='post_delete'),
    path('posts/<int:pk>/comments/add', views.add_comment_post, name='add_comment_post'),
    path('posts/<int:pk>/comments/edit/<int:comment_pk>', views.edit_comment_post, name='edit_comment_post'),
    path('posts/<int:pk>/comments/delete/<int:comment_pk>', views.delete_comment_post, name='delete_comment_post'),
    path('photos/api/v1/photo/<int:pk>/add_like', views.add_like, name='add_like'),


    
]