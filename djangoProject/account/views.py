from django.shortcuts import HttpResponseRedirect, reverse, render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, auth
from account.forms import ProfileForm, MyUserForm
from django.contrib.auth.decorators import login_required
from django.views import generic
from account.models import Profile
from .forms import SignUpForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # successfully login
            login(request, user)
            if request.GET.get("next"):
                return HttpResponseRedirect(request.GET.get("next"))
            return HttpResponseRedirect(reverse("home"))
        else:
            context = {
                "username": username
            }
    else:
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse("home"))
        context = {}
    return render(request, "account/login.html", context)


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))


#
# def register(request):
#     if request.method == "POST":
#         first_name = request.POST["first_name"]
#         last_name = request.POST["last_name"]
#         user_name = request.POST["username"]
#         password1 = request.POST["password1"]
#         password2 = request.POST["password2"]
#         email = request.POST["email"]
#         if password1 == password2:
#             if User.objects.filter(username=user_name).exists():
#                 messages.info(request, "نام کاربری واردشده قبلا استفاده شده است")
#                 return HttpResponseRedirect(reverse("register"))
#             elif User.objects.filter(email=email).exists():
#                 messages.info(request, "ایمیل وارد شده قبلا استفاده شده است")
#                 return HttpResponseRedirect(reverse("register"))
#             else:
#                 user = User.objects.create_user(username=user_name, password=password1, email=email, first_name=first_name, last_name=last_name)
#                 user.save()
#                 messages.info(request, "کاربر جدید ساخته شد")
#                 return HttpResponseRedirect(reverse("home"))
#         else:
#             messages.info(request, "رمزهای وارد شده مطابقت ندارند")
#             return HttpResponseRedirect(reverse("register"))
#     else:
#         return render(request, "account/register.html")


class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'account/register.html'
    success_url = reverse_lazy('login')


# def UserRegisterView(request):
#     form = SignUpForm
#     context = {
#         "form": form,
#         "messages": messages
#     }
#     return render(request, "account/register.html", context)
#

@login_required
def profile_details(request):
    profile = request.user.profile
    context = {
        "profile": profile
    }
    return render(request, "account/profile_details.html", context)


@login_required
def profile_edit(request):
    if request.method == "POST":
        profile_form = ProfileForm(request.POST, files=request.FILES, instance=request.user.profile)
        user_form = MyUserForm(request.POST, instance=request.user)
        if profile_form.is_valid() and user_form.is_valid():
            profile_form.save()
            user_form.save()
            return HttpResponseRedirect(reverse("profile_details"))
    else:
        profile_form = ProfileForm(instance=request.user.profile)
        user_form = MyUserForm(instance=request.user)
    context = {
        "profile_form": profile_form,
        "user_form": user_form
    }
    return render(request, "account/profile_edit.html", context)


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            return redirect('changepassword')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'account/change_password.html', {
        'form': form
    })
