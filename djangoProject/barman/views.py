from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth import authenticate, login, logout
from barman.forms import ContactForm


from barman.models import Ab, Cont
from sample.models import Sample, Subsample
from services.models import Service, Sub


def home(request):
    services = Service.objects.all()
    sub_services = Sub.objects.all()
    samples = Sample.objects.all()
    subsamples = Subsample.objects.all()
    context = {
        "services": services,
        "sub_services": sub_services,
        "samples": samples,
        "subsamples": subsamples
    }

    return render(request, "barman/home.html", context)


def about(request):
    aboutt = Ab.objects.get(pk=1)
    services = Service.objects.all()
    sub_services = Sub.objects.all()
    samples = Sample.objects.all()
    subsamples = Subsample.objects.all()
    context = {
        "aboutt": aboutt,
        "services": services,
        "sub_services": sub_services,
        "samples": samples,
        "subsamples": subsamples
    }
    return render(request, "barman/about.html", context)


def contact(request):
    samples = Sample.objects.all()
    subsamples = Subsample.objects.all()
    services = Service.objects.all()
    sub_services = Sub.objects.all()
    # contactus = Cont.objects.get(telegram="diyabetshap")
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ContactForm()
    context = {
        # "contactus": contactus,
        'form': form,
        "services": services,
        "sub_services": sub_services,
        "samples": samples,
        "subsamples": subsamples
    }
    return render(request, "barman/contact.html", context)

