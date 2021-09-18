from django.core.paginator import Paginator, EmptyPage
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.views.generic import ListView

from news.models import News, Tag, Category


def news(request):
    new = News.objects.all().order_by("-publish_date")
    p = Paginator(new, 2)
    page_num = request.GET.get('page', 1)
    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)
    tags = Tag.objects.all()
    categories = Category.objects.all()
    last_news = News.objects.order_by("-publish_date")[0:3]
    context = {
        "new": page,
        "tags": tags,
        "categories": categories,
        "last_news": last_news,
    }
    return render(request, "news/news.html", context)


class SearchList(ListView):
    template_name = "news/search_list.html"

    def get_queryset(self):
        search = self.request.GET.get('q')
        # return News.objects.filter(title__contains=search)
        return News.objects.filter(description__contains=search)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search'] = self.request.GET.get('q')
        context["tags"] = Tag.objects.all()
        context["last_news"] = News.objects.order_by("-publish_date")[0:3]
        context["categories"] = Category.objects.all()
        return context


def news_detail(request, new_id):
    new = get_object_or_404(News, pk=new_id)
    tags = Tag.objects.all()
    categories = Category.objects.all()
    last_news = News.objects.order_by("-publish_date")[0:3]
    context = {
        "new": new,
        "tags": tags,
        "categories": categories,
        "last_news": last_news,
    }
    return render(request, "news/news_detail.html", context)


def tag_news(request, tag_id):
    tag = get_object_or_404(Tag, pk=tag_id)
    tags = Tag.objects.all()
    categories = Category.objects.all()
    last_news = News.objects.order_by("-publish_date")[0:3]
    new = News.objects.all().order_by("-publish_date")
    context = {
        "tag": tag,
        "tags": tags,
        "categories": categories,
        "last_news": last_news,
        "new": new,
    }
    return render(request, "news/tag_news.html", context)


def category_news(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    tags = Tag.objects.all()
    categories = Category.objects.all()
    last_news = News.objects.order_by("-publish_date")[0:3]
    new = News.objects.all().order_by("-publish_date")
    context = {
        "tags": tags,
        "category": category,
        "categories": categories,
        "last_news": last_news,
        "new": new,
    }
    return render(request, "news/caregory_news.html", context)
