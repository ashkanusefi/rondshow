from django.shortcuts import render, get_object_or_404, HttpResponse, HttpResponseRedirect
from news.models import New
from .forms import NewsCommentForm
from services.models import Service, Sub
from sample.models import Subsample, Sample
from django.contrib.auth.decorators import login_required


def ne(request):
    news = New.objects.all()
    sub_services = Sub.objects.all()
    services = Service.objects.all()
    samples = Sample.objects.all()
    subsamples = Subsample.objects.all()
    context = {
        "news": news,
        "services": services,
        "sub_services": sub_services,
        "samples": samples,
        "subsamples": subsamples
    }
    return render(request, "news/news.html", context)


#
#
# def news_detail(request, new_id):
#     news_details = get_object_or_404(New, pk=new_id)
#     sub_services = Sub.objects.all()
#     services = Service.objects.all()
#     samples = Sample.objects.all()
#     subsamples = Subsample.objects.all()
#     context = {
#         "news_details": news_details,
#         "services": services,
#         "sub_services": sub_services,
#         "samples": samples,
#         "subsamples": subsamples
#     }
#     return render(request, "news/news_detail.html", context)
#


def news_detail(request, new_id):
    news_details = get_object_or_404(New, pk=new_id)
    sub_services = Sub.objects.all()
    services = Service.objects.all()
    samples = Sample.objects.all()
    subsamples = Subsample.objects.all()
    # post = get_object_or_404(New, slug=slug)
    # if request.user.is_authenticated and request.user.is_active:
    comments = news_details.comment_News.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = NewsCommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = news_details
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = NewsCommentForm()
    context = {
        "news_details": news_details,
        "services": services,
        "sub_services": sub_services,
        "samples": samples,
        "subsamples": subsamples,
        # 'post': post,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form
    }
    return render(request, "news/news_detail.html", context)


#
# def post_detail(request, slug):
#     template_name = 'post_detail.html'
#     post = get_object_or_404(New, slug=slug)
#     comments = post.comments.filter(active=True)
#     new_comment = None
#     # Comment posted
#     if request.method == 'POST':
#         comment_form = CommentForm(data=request.POST)
#         if comment_form.is_valid():
#             # Create Comment object but don't save to database yet
#             new_comment = comment_form.save(commit=False)
#             # Assign the current post to the comment
#             new_comment.post = post
#             # Save the comment to the database
#             new_comment.save()
#     else:
#         comment_form = CommentForm()
#
#     return render(request, "news/comment.html", {'post': post,
#                                                  'comments': comments,
#                                                  'new_comment': new_comment,
#                                                  'comment_form': comment_form})
