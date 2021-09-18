from django.shortcuts import render, get_object_or_404
from services.models import Service, Sub
from sample.models import Sample, Subsample


def ser(request):
    services = Service.objects.all()
    sub_services = Sub.objects.all()
    samples = Sample.objects.all()
    subsamples = Subsample.objects.all()
    context = {
        'services': services,
        "sub_services": sub_services,
        "samples": samples,
        "subsamples": subsamples
    }
    return render(request, "services/services.html", context)


def services_detail(request, service_id):
    service_detail = get_object_or_404(Service, pk=service_id)
    services = Service.objects.all()
    sub_services = Sub.objects.all()
    samples = Sample.objects.all()
    subsamples = Subsample.objects.all()
    context = {
        "service_detail": service_detail,
        "sub_services": sub_services,
        'services': services,
        "samples": samples,
        "subsamples": subsamples

    }
    return render(request, "services/services_detail.html", context)


def subservice_detail(request, sub_service_id):
    subservice_details = get_object_or_404(Sub, pk=sub_service_id)
    services = Service.objects.all()
    sub_services = Sub.objects.all()
    samples = Sample.objects.all()
    subsamples = Subsample.objects.all()
    context = {
        "subservice_details": subservice_details,
        'services': services,
        "sub_services": sub_services,
        "samples": samples,
        "subsamples": subsamples
    }
    return render(request, "services/sub_service_detail.html", context)
