# from ckeditor.fields import RichTextField
from django.db import models
from django.utils.html import format_html


class Tag(models.Model):
    class Meta:
        verbose_name = "تگ"
        verbose_name_plural = "تگ"

    tag = models.CharField("تگ", max_length=100)

    def __str__(self):
        return self.tag


class Category(models.Model):
    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی"

    category = models.CharField("نام دسته بندی", max_length=70)

    def __str__(self):
        return self.category


class News(models.Model):
    class Meta:
        verbose_name = "خبر"
        verbose_name_plural = "خبر"

    name = models.CharField("نام خبر", max_length=70)
    title = models.CharField("عنوان خبر", max_length=500)
    image = models.ImageField("عکس خبر", upload_to="images/")
    description = models.TextField("متن خبر")
    publish_date = models.DateTimeField("تاریخ انتشار", auto_now_add=True)
    tag = models.ManyToManyField(Tag, verbose_name="تگ مربوطه")
    category = models.ManyToManyField(Category, verbose_name="نام دسته بندی")

    def __str__(self):
        return self.name

    def thumbnail(self):
        return format_html("<img width=50 height=30 style='border-radius: 5px;' src='{}'>".format(self.image.url))

    thumbnail.short_description = "تصویر"
