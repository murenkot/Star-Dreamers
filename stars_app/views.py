from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.contrib.auth.decorators import login_required 

# import Models
from .models import Photo


# for API requests:
import requests 
import datetime


# Create your views here.

def main_page(request):
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
        # at first check if day photo is not in DB
        date_record = Photo.objects.filter(date = photo['date']).exists()
        if date_record == False:
            new_photo = Photo(date=photo['date'], explanation = photo['explanation'], title = photo['title'], url = photo['url'])
            new_photo.save()

    # get 20 last photos from DB:
    last_20 = Photo.objects.all().order_by('-id')[:20]
    context = {'photos':last_20}
    return render(request, 'main_page.html', context)

def photo_details(request, pk):
    photo = Photo.objects.get(id=pk)
    context = {"photo":photo}
    return render(request, 'photo_page.html', context)