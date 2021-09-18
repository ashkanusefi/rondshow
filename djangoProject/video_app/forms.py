from .models import CommentOfVideos
from django import forms


class VideoCommentForm(forms.ModelForm):
    class Meta:
        model = CommentOfVideos
        fields = ('name', 'email', 'body')
