from .models import CommentOfArticle
from django import forms


class ArticleCommentForm(forms.ModelForm):
    class Meta:
        model = CommentOfArticle
        fields = ('name', 'email', 'body')
