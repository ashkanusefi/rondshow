from django.shortcuts import render, get_object_or_404
from sample.models import Sample, Subsample
from services.models import Service, Sub


def samp(request):
    services = Service.objects.all()
    sub_services = Sub.objects.all()
    samples = Sample.objects.all()
    subsamples = Subsample.objects.all()
    context = {
        "samples": samples,
        "services": services,
        "sub_services": sub_services,
        "subsamples": subsamples
    }
    return render(request, "sample/sample.html", context)


def samples_detail(request, sample_id):
    sample_detail = get_object_or_404(Sample, pk=sample_id)
    services = Service.objects.all()
    sub_services = Sub.objects.all()
    samples = Sample.objects.all()
    subsamples = Subsample.objects.all()
    context = {
        "sample_detail": sample_detail,
        "sub_services": sub_services,
        'services': services,
        "samples": samples,
        "subsamples": subsamples

    }
    return render(request, "sample/sample_details.html", context)


def subsample_detail(request, subsample_id):
    subsample_details = get_object_or_404(Subsample, pk=subsample_id)
    services = Service.objects.all()
    sub_services = Sub.objects.all()
    samples = Sample.objects.all()
    subsamples = Subsample.objects.all()
    context = {
        "sub_services": sub_services,
        'services': services,
        "subsample_details": subsample_details,
        "samples": samples,
        "subsamples": subsamples

    }
    return render(request, "sample/subsample_details.html", context)
