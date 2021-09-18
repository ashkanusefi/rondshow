from django.db import models


class New(models.Model):
    class Meta:
        verbose_name = 'اخبار'
        verbose_name_plural = 'اخبار'

    title = models.CharField("عنوان خبر", max_length=300)
    description = models.TextField("توضیحات خبر")
    image = models.ImageField("تصویر خبر", upload_to="image_uploaded/")

    def __str__(self):
        return self.title


class CommentOfNews(models.Model):
    post = models.ForeignKey(New, on_delete=models.CASCADE, related_name='comment_News', verbose_name="عنوان خبر")
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
