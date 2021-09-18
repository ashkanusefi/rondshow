from django.shortcuts import render, get_object_or_404

from article.models import Article
from services.models import Service, Sub
from sample.models import Sample, Subsample
from .forms import ArticleCommentForm


def art(request):
    articles = Article.objects.all()
    services = Service.objects.all()
    sub_services = Sub.objects.all()
    samples = Sample.objects.all()
    subsamples = Subsample.objects.all()
    context = {
        'articles': articles,
        "services": services,
        "sub_services": sub_services,
        "samples": samples,
        "subsamples": subsamples
    }
    return render(request, "article/article.html", context)


def article_detail(request, article_id):
    article_details = get_object_or_404(Article, pk=article_id)
    services = Service.objects.all()
    sub_services = Sub.objects.all()
    samples = Sample.objects.all()
    subsamples = Subsample.objects.all()
    # post = get_object_or_404(New, slug=slug)
    comments = article_details.comment_Article.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = ArticleCommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = article_details
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = ArticleCommentForm()

    context = {
        "article_details": article_details,
        "services": services,
        "sub_services": sub_services,
        "samples": samples,
        "subsamples": subsamples,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form
    }
    return render(request, "article/article_details.html", context)
