from django.urls import path, re_path
from .views import ArticleList, ArticleDetail, ArticlePreview, CategoryList, AuthorList

app_name = "blog"
urlpatterns = [
    path('', ArticleList.as_view(), name='home'),
    path('page/<int:page>', ArticleList.as_view(), name='home'),
    re_path(r'^article/(?P<slug>[-\w]+)', ArticleDetail.as_view(), name='detail'),
    path('preview/<int:pk>', ArticlePreview.as_view(), name='preview'),
    re_path(r'^categories/(?P<slug>[-\w]+)', CategoryList.as_view(), name='category'),
    re_path(r'^category/(?P<slug>[-\w]+)/page/(?P<page>\d+)', CategoryList.as_view(), name='category'),
    path('author/<slug:username>', AuthorList.as_view(), name='author'),
    path('author/<slug:username>/page/<int:page>', AuthorList.as_view(), name='author'),
]
