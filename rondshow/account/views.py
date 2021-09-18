from django.shortcuts import render


def account(request):
    return render(request, 'account.html', {})


def app(request):
    return render(request, 'account.html', {})
