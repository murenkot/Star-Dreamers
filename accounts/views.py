from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from django.contrib import auth
from stars_app.models import Profile, Post
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
                context = { 'error': 'Invalid User' }
                return render (request, 'register.html', context)
            else:
                if User.objects.filter(email=email).exists():
                    context = {'error': 'This email is not valid.' }
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
            context = { 'error': 'Your password doesnt match. Please confirm again' }
            return render(request, 'register.html', context)

    else:
        return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username = username, password = password)
        if username is not None:
            auth.login(request, user)
            return redirect ('main_page')
        else:
            context = { 'error': 'Invalid Login' }
            return render (request, 'login.html', context)
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('main_page')

def profile(request):
    post = Post.objects.filter(user=request.user)
    context = {'post': post}
    return render(request, 'profiles.html', context)





