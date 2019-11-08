from django.contrib import admin

from .models import Post, CommentPhoto, CommentPost, LikePhoto, LikePost, Profile

# Register your models here.
admin.site.register(Post)
admin.site.register(CommentPhoto)
admin.site.register(CommentPost)
admin.site.register(LikePhoto)
admin.site.register(LikePost)
admin.site.register(Profile)
