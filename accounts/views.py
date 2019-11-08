from django.contrib.auth.decorators import login_required 
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.core import serializers

from django.contrib.auth.models import User
from django.contrib import auth
from stars_app.models import Post, Profile
from stars_app.forms import ProfileForm
# Create your views here.

def welcome(request):
    return render (request, 'welcome.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(username=username).exists():
                context = { 'error': 'This user name has been used' }
                return render (request, 'register.html', context)
            else:
                if User.objects.filter(email=email).exists():
                    context = {'error': 'This email is not valid. Please try again' }
                    return render(request, 'register.html', context)
                else:
                    user = User.objects.create_user(
                        first_name = first_name,
                        last_name = last_name,
                        username = username,
                        email = email,
                        password = password)
                    user.save()
                    return redirect ('main_page')
        else:
            context = { 'error': 'Your password did not match. Please try again' }
            return render(request, 'register.html', context)

    else:
        return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username = username, password = password)
        if user is not None:
            auth.login(request, user)
            return redirect ('main_page')
        else:
            context = { 'error': 'Your username and password does not match. Please try again.' }
            return render (request, 'login.html', context)
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('main_page')

@login_required(login_url='/login/')
def profile(request):
    current_user = request.user.pk
    current_user_name = request.user.username
    posts = Post.objects.filter(user=current_user)
    context = {"posts": posts, "author": current_user_name }
    return render(request, 'profile.html', context)

def profile_create(request):
    if request.method == 'POST':
        avatar = request.POST['avatar']
        userstory = request.POST['userstory']
        
        if Profle.objects.filter(pk=id).exist():
            profile = Profile.objects(
                avatar = avatar,
                userstory = userstory,
                user = request.user)
            profile.save()

        else:
            profile = Profile.objects.create(
                avatar = avatar,
                userstory = userstory,
                user = request.user)
            profile.save()
            return redirect('profile')






