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

class CommentPhoto(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="photocomments_user")
    body = models.TextField()
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE, related_name="photocomments_photo")

class LikePhoto(models.Model):
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE, related_name="photolikes_photo")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="photolikes_user")

class LikePost(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="postlikes_post")
    user = models.ForeignKey(Photo, on_delete=models.CASCADE, related_name="postlikes_user")

class Profile(models.Model):
    avatar = models.TextField()
    userstory = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="profiles_user")

class CommentPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="postcomments_user")
    body = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="postcomments_post")


