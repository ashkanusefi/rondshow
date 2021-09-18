"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, re_path, include
from barman.views import about, contact, home
from django.conf import settings
from video_app.views import vid, videos_detail
from sample.views import samp, samples_detail, subsample_detail
from article.views import art, article_detail
from news.views import news_detail, ne
from services.views import ser, services_detail, subservice_detail
from account.views import logout_view, login_view, profile_details, profile_edit, UserRegisterView, change_password
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("about/", about, name="about"),
    path("", home, name="home"),
    path("contact/", contact, name="contact"),
    path("video/", vid, name="videos"),
    path("article/", art, name="articles"),
    path("news/", ne, name="news"),
    path("services/", ser, name="services"),
    path("services/detail/<int:service_id>/", services_detail, name="services_detail"),
    path("subservice/detail/<int:sub_service_id>/", subservice_detail, name="sub_service_detail"),
    path("sample/", samp, name="samples"),
    path("subsample/detail/<int:subsample_id>/", subsample_detail, name="subsample_detail"),
    path("sample/detail/<int:sample_id>/", samples_detail, name="sample_detail"),
    path("article/detail/<int:article_id>/", article_detail, name="article_detail"),
    path("news/detail/<int:new_id>/", news_detail, name="news_details"),
    path("video/details/<int:video_id>/", videos_detail, name="video_detail"),
    path("accounts/login/", login_view, name="login"),
    path("accounts/logout/", logout_view, name="logout"),
    path("accounts/register", UserRegisterView.as_view(), name="register"),
    path("accounts/profile_details", profile_details, name="profile_details"),
    path("accounts/profile_edit", profile_edit, name="profile_edit"),
    path("accounts/change_password/", change_password, name="changepassword"),
    path("reset_password/", auth_views.PasswordResetView.as_view(), name="reset_password"),
    path("reset_password_sent/", auth_views.PasswordResetDoneView.as_view(), name="reset_password_sent"),
    path("reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path("reset_password_complete/", auth_views.PasswordResetCompleteView.as_view(), name="reset_password_complete"),
    re_path(r'^ratings/', include('star_ratings.urls', namespace='ratings')),
]

if settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
