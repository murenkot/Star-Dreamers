from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Photo(models.Model):
    date = models.CharField(max_length=20)
    title = models.CharField(max_length=100)
    explanation = models.TextField()
    url = models.TextField()
    hdurl = models.TextField()

class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts_user")
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE, related_name="posts_photo")

class Comment(models.Model):
    title = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments_user")
    body = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments_post")

class Like(models.Model):
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE, related_name="likes_photo")
    user = models.ForeignKey(Photo, on_delete=models.CASCADE, related_name="likes_user")

class Profile(models.Model):
    avatar = models.TextField()
    userstory = models.TextField()
    user = models.ForeignKey(Photo, on_delete=models.CASCADE, related_name="profiles_user")
