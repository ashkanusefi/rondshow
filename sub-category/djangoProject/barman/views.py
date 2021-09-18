from django.shortcuts import render

from barman.models import Menu


def test(request):
    main_menu = Menu.objects.filter(parent__isnull=True)
    return render(request, "barman/khadamat_test.html", {"menus": main_menu})
