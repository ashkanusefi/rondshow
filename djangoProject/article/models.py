from django.db import models


class Article(models.Model):
    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقاله'

    title = models.CharField("عنوان مقاله", max_length=500)
    text = models.TextField("مقاله")
    image = models.ImageField("تصویر مقاله", upload_to='image_uploaded/')

    def __str__(self):
        return self.title


class CommentOfArticle(models.Model):
    post = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comment_Article', verbose_name="عنوان مقاله")
    name = models.CharField("نام", max_length=80)
    email = models.EmailField("ایمیل")
    body = models.TextField("متن")
    created_on = models.DateTimeField("تاریخ ایجاد دیدگاه", auto_now_add=True)
    active = models.BooleanField("انتشار", default=False)

    class Meta:
        ordering = ['created_on']
        verbose_name = "نظرات"
        verbose_name_plural = "نظرات"

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)
