from django.db import models
from django.urls import reverse
from account.models import User
from django.utils import timezone
from extensions.utils import jalali_converter
from django.utils.html import format_html


# costume manager
class ArticleManager(models.Manager):
    def published(self):
        return self.filter(status='p')


class CategoryManager(models.Manager):
    def active(self):
        return self.filter(status=True)


# Create your models here.
class Category(models.Model):
    parent = models.ForeignKey('self', default=None, null=True, blank=True, on_delete=models.SET_NULL,
                               related_name='children', verbose_name="زیر دسته")
    title = models.CharField(max_length=200, verbose_name='عنوان دسته بندی')
    slug = models.SlugField(max_length=200, allow_unicode=True, unique=True, verbose_name='آدرس دسته بندی')
    status = models.BooleanField(default=True, verbose_name='آیا نمایش داده شود؟')
    position = models.IntegerField(verbose_name="پوزیشن")

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'
        ordering = ['parent__id', 'position']

    def __str__(self):
        return self.title

    objects = CategoryManager()


class Articles(models.Model):
    STATUS_CHOICES = (
        ('d', 'پیش نویس'),        # draft
        ('p', 'منتشر شده'),       # published
        ('i', 'بررسی'),    # investigation
        ('b', 'برگشت داده شده'),  # back
    )
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='articles',
                               verbose_name='نویسنده')
    title = models.CharField(max_length=200, verbose_name='عنوان مقاله')
    slug = models.SlugField(max_length=200, allow_unicode=True, unique=True, verbose_name='آدرس مقاله')
    category = models.ManyToManyField(Category, verbose_name='دسته بندی', related_name='articles')
    description = models.TextField(verbose_name='محتوا')
    admincomment = models.TextField(null=True, blank=True, verbose_name='توضیحات اضافه (این قسمت در وب سایت نمایش داده نمیشود)')
    thumbnail = models.ImageField(upload_to='images', verbose_name='تصویر')
    publish = models.DateTimeField(default=timezone.now, verbose_name='زمان انتشار')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_special = models.BooleanField(default=False, verbose_name='مقاله ویژه')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, verbose_name='وضعیت')

    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'
        ordering = ['-publish']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("account:home")

    def jpublish(self):
        return jalali_converter(self.publish)

    jpublish.short_description = 'زمان انتشار'

    def thumbnail_tag(self):
        return format_html('<img height=70 style=border-radius:5px src="{}">'.format(self.thumbnail.url))

    thumbnail_tag.short_description = 'عکس'

    def category_to_str(self):
        return "، ".join([category.title for category in self.category.active()])

    category_to_str.short_description = 'دسته بندی'

    objects = ArticleManager()
