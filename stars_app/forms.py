from django import forms
from .models import CommentPhoto, CommentPost

class CommentPhotoForm(forms.ModelForm):

    class Meta:
        model = CommentPhoto
        fields = ('body', )


class CommentPostForm(forms.ModelForm):

    class Meta:
        model = CommentPost
        fields = ('body', )
