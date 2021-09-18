from django.shortcuts import render, get_object_or_404
from video_app.models import Videos
from services.models import Service, Sub
from sample.models import Sample, Subsample
from .forms import VideoCommentForm


def vid(request):
    videos = Videos.objects.all()
    services = Service.objects.all()
    sub_services = Sub.objects.all()
    samples = Sample.objects.all()
    subsamples = Subsample.objects.all()
    context = {
        "videos": videos,
        "services": services,
        "sub_services": sub_services,
        "samples": samples,
        "subsamples": subsamples
    }
    return render(request, "video_app/video.html", context)


def videos_detail(request, video_id):
    video_detail = get_object_or_404(Videos, pk=video_id)
    services = Service.objects.all()
    sub_services = Sub.objects.all()
    samples = Sample.objects.all()
    subsamples = Subsample.objects.all()
    comments = video_detail.comment_Videos.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = VideoCommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = video_detail
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = VideoCommentForm()
    context = {
        "video_detail": video_detail,
        "sub_services": sub_services,
        'services': services,
        "samples": samples,
        "subsamples": subsamples,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form
    }
    return render(request, "video_app/videos_detail.html", context)
