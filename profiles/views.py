from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from django.contrib import Post

# Create your views here.

def post_details (request, pk):
    post = Post.objects.get(id=pk)
    context = { 'post': post }
    return render (request, 'profile.html', context)