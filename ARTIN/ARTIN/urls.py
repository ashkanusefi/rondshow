"""ARTIN URL Configuration

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
from django.conf import settings
from django.contrib import admin
from django.urls import path

from index.views import home
from news.views import news, news_detail, tag_news, category_news, SearchList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('news/', news, name="news"),
    path('news_details/<int:new_id>/', news_detail, name="news_details"),
    path("tag_news/<int:tag_id>/", tag_news, name="tag_news"),
    path("category_news/<int:category_id>/", category_news, name="category_news"),
    path("search/", SearchList.as_view(), name="search"),
]

if settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
