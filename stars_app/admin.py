from django.contrib import admin

from .models import Post, CommentPhoto, CommentPost, Like, Profile

# Register your models here.
admin.site.register(Post)
admin.site.register(CommentPhoto)
admin.site.register(CommentPost)
admin.site.register(Like)
admin.site.register(Profile)
