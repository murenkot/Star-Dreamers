from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.contrib.auth.decorators import login_required 
from django.views.decorators.csrf import csrf_exempt

# import Models
from .models import Photo, CommentPhoto, CommentPost, Post, LikePhoto, LikePost, User
from .forms import CommentPhotoForm, CommentPostForm, PostForm


# for API requests:
import requests 
import datetime


# Create your views here.

def count_photo_likes(pk):
    photo = Photo.objects.get(id=pk)
    likes = LikePhoto.objects.filter(photo = photo)
    return len(likes)

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
            new_photo = Photo(date=photo['date'], explanation = photo['explanation'], title = photo['title'], url = photo['hdurl'])
            new_photo.save()

    # get 20 last photos from DB:
    last_20 = Photo.objects.all().order_by('-id')[:20]
    likes_list = []


    # @login_required
    for photo in last_20:
        like = LikePhoto.objects.filter(photo=photo, user=request.user)
        if len(like)>0:
            checked = "-checked"
            likes_list.append(checked)
        else:
            checked = " "
            likes_list.append(checked)
    zipped_list = list(zip(last_20, likes_list))
    context = {'photos':last_20, "checked": likes_list, 'zipped_list': zipped_list}
    return render(request, 'main_page.html', context)

def all_posts(request):
    posts_20 = Post.objects.all().order_by('-id')[:20]
    likes_list = []
    for post in posts_20:
        like = LikePost.objects.filter(post=post, user=request.user)
        if len(like)>0:
            checked = "-checked"
            likes_list.append(checked)
        else:
            checked = " "
            likes_list.append(checked)
    zipped_list = list(zip(posts_20, likes_list))
    context = {'posts':posts_20, "checked": likes_list, 'zipped_list': zipped_list}
    return render(request, 'posts_page.html', context)



def photo_details(request, pk):
    photo = Photo.objects.get(id=pk)
    likes = count_photo_likes(pk)
    comments = len(CommentPhoto.objects.filter(photo = photo))
    like = LikePhoto.objects.filter(photo=photo, user=request.user)
    if len(like)>0:
        checked = "-checked"
    else:
        checked = " "
    context = {"photo":photo, "likes":likes, "comments":comments, "checked":checked}
    return render(request, 'photo_page.html', context)

@login_required
@csrf_exempt
def add_comment(request, pk, comment):
    print("adding comment")
    photo = Photo.objects.get(id=pk)
    if request.method == 'POST':
        new_comment = CommentPhoto(user=request.user, body=comment, photo=photo)
        new_comment.save()
        print(new_comment.pk)
        data = {"username": request.user.username, "body": comment, 'photo_pk':photo.pk,  "comment_pk": new_comment.pk}
        return JsonResponse({'data': data, 'status':200})
    
@login_required
def edit_comment(request, pk, comment_pk):
    photo = Photo.objects.get(id=pk)
    comment = CommentPhoto.objects.get(id=comment_pk)
    if request.method == 'POST':
        form = CommentPhotoForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save()
            return redirect('photo_details', pk=pk)
    else:
        form = CommentPhotoForm(instance=comment)
    context = {'form': form, 'photo':photo, 'comment':comment, 'header': f"Edit your comment"}
    return render(request, 'photo_comment_form.html', context)

@login_required
def delete_comment(request, pk, comment_pk):
    CommentPhoto.objects.get(id=comment_pk).delete()
    return redirect('photo_details', pk=pk)

@login_required
def create_post(request, pk):
    photo = Photo.objects.get(id=pk)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.photo = photo
            post.user = request.user
            post.save()
        return redirect('post_details', pk=post.pk)
    else: 
        form = PostForm()
    context = {'form': form, "post":form, "photo":photo, 'header':f"Share your dreams"}
    return render(request, 'post_form.html', context)

def post_details(request, pk):
    post = Post.objects.get(id=pk)
    likes = len(LikePost.objects.filter(post=post))
    comments = len(CommentPost.objects.filter(post = post))
    like = LikePost.objects.filter(post=post, user=request.user)
    if len(like)>0:
        checked = "-checked"
    else:
        checked = " "
    context = {"post":post, "likes":likes, "comments":comments, "checked":checked}    
    return render(request, 'post.html', context)

@login_required
def post_edit(request, pk):
    post = Post.objects.get(id=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect('post_details', pk=pk)
    else:
        form = PostForm(instance=post)
    context = {'form': form, 'post':post, 'header': f"Edit your post"}
    return render(request, 'post_edit_form.html', context)

@login_required
def post_delete(request, pk):
    Post.objects.get(id=pk).delete()
    return redirect('main_page')


@login_required
@csrf_exempt
def add_comment_post(request, pk, comment):
    post = Post.objects.get(id=pk)
    if request.method == 'POST':
        new_comment = CommentPost(user=request.user, body=comment, post=post)
        new_comment.save()
        print(new_comment.pk)
        data = {"username": request.user.username, "body": comment, 'post_pk':post.pk,  "comment_pk": new_comment.pk}
        return JsonResponse({'data': data, 'status':200})
    

@login_required
def edit_comment_post(request, pk, comment_pk):
    post = Post.objects.get(id=pk)
    comment = CommentPost.objects.get(id=comment_pk)
    if request.method == 'POST':
        form = CommentPostForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save()
            return redirect('post_details', pk=comment.post.pk)
    else:
        form = CommentPostForm(instance=comment)
    context = {'form': form, 'post':post, 'comment':comment, 'header': f"Edit your comment"}
    return render(request, 'post_comment_form.html', context)

@login_required
def delete_comment_post(request, pk, comment_pk):
    CommentPost.objects.get(id=comment_pk).delete()
    return redirect('post_details', pk=pk)

@login_required
@csrf_exempt
def add_like(request, pk):
    user = request.user
    photo = Photo.objects.get(id=pk)
    user_likes = LikePhoto.objects.filter(photo=photo, user=user)
    if len(user_likes) == 0:
        like = LikePhoto(photo=photo, user=user)
        like.save()
    else:
        user_likes.delete()
    likes = count_photo_likes(pk)
    context = {"likes":likes}
    return JsonResponse({'data':context, "status":200})


@login_required
@csrf_exempt
def add_like_post(request, pk):
    user = request.user
    post = Post.objects.get(id=pk)
    user_likes = LikePost.objects.filter(post=post, user=user)
    if len(user_likes) == 0:
        like = LikePost(post=post, user=user)
        like.save()
    else:
        user_likes.delete()
    likes = len(LikePost.objects.filter(post = post))
    context = {"likes":likes}
    return JsonResponse({'data':context, "status":200})



