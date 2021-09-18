from .models import CommentOfNews
from django import forms


class NewsCommentForm(forms.ModelForm):
    class Meta:
        model = CommentOfNews
        fields = ('name', 'email', 'body')
