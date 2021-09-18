from django.shortcuts import render

from index.forms import Contact_Form
from index.models import Questions, Main_pic, Advisor


def home(request):
    advisors = Advisor.objects.all()
    # questions = Questions.objects.all()
    x = int(Questions.objects.count() / 2)
    right_questions = Questions.objects.all()[:x]
    left_questions = Questions.objects.all()[x:]
    mainpics = Main_pic.objects.all()
    form = Contact_Form(request.POST or None)
    if form.is_valid():
        form.save()
        form = Contact_Form()
    context = {
        # "questions": questions,
        "form": form,
        "mainpics": mainpics,
        "advisors": advisors,
        "right_questions": right_questions,
        "left_questions": left_questions,
    }
    return render(request, "index/home.html", context)
