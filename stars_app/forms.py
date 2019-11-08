from django import forms
from .models import CommentPhoto, CommentPost, Post, Profile

class CommentPhotoForm(forms.ModelForm):

    class Meta:
        model = CommentPhoto
        fields = ('body', )


class CommentPostForm(forms.ModelForm):

    class Meta:
        model = CommentPost
        fields = ('body', )

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'body')

class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('avatar', 'userstory')