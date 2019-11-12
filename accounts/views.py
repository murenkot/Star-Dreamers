from django.contrib.auth.decorators import login_required 
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.core import serializers

from django.contrib.auth.models import User
from django.contrib import auth
from stars_app.models import Post, Profile, Photo
from stars_app.forms import ProfileForm
# Create your views here.

import requests 
import datetime

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
                    return render(request, 'login.html')
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
            return render(request, 'login.html', context)
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('login')

@login_required(login_url='/login/')
def profile(request):
    posts = Post.objects.filter(user=request.user)
    try: 
        profile = Profile.objects.get(user=request.user)
        context = { "posts": posts, "profile": profile }
        return render(request, 'profile.html', context)
    except Profile.DoesNotExist:
        context = { "posts": posts }
        return render(request, 'profile.html', context)

def profile_create(request):
    if request.method == 'POST':
        avatar = request.POST['avatar']
        userstory = request.POST['userstory']
        try: 
            profile = Profile.objects.get(user=request.user)
            profile.avatar = avatar
            profile.userstory = userstory
            profile.save()
            return redirect('profile')
        except Profile.DoesNotExist:
            profile = Profile.objects.create(
            avatar = avatar,
            userstory = userstory,
            user = request.user)
            profile.save()
            return redirect('profile')

@login_required
def profile_show(request, pk):
    posts = Post.objects.filter(user=pk)
    author = User.objects.get(id=pk)
    profile = Profile.objects.get(user=pk)
    context = {'posts': posts, 'author': author, 'profile': profile }
    return render(request, 'author_profile.html', context)


def guest_login(request):
    current_date = datetime.datetime.today()
    one_day = datetime.timedelta(days=1)
    end_date = current_date.strftime('%Y-%m-%d')
    start_date = (current_date - one_day*20).strftime('%Y-%m-%d')

    """ NASA API """
    api_key = "WvjNlI8EFTS53dSAK4MKnJO4dAWKqwP1pNcjAfPK"
    url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}&start_date={start_date}&end_date={end_date}"

    payload = ""
    headers = {
        'x-rapidapi-host': "NasaAPIdimasV1.p.rapidapi.com",
        'x-rapidapi-key': "75e8b98d64msh7c71a65cb0fbfd7p12a3b5jsn2896b7bca1de",
        'content-type': "application/x-www-form-urlencoded"
        }

    response = requests.get(url, data=payload, headers=headers).json()

    for photo in response:
        date_record = Photo.objects.filter(date = photo['date']).exists()
        if date_record == False:
            new_photo = Photo(date=photo['date'], explanation = photo['explanation'], title = photo['title'], url = photo['url'])
            new_photo.save()

    last_20 = Photo.objects.all().order_by('-id')[:20]
    context = {'photo':last_20}
    return render(request, 'main_page.html', context) 

