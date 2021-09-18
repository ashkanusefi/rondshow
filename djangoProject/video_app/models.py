from django.db import models


class Videos(models.Model):
    class Meta:
        verbose_name = "ویدئوها"
        verbose_name_plural = "ویدئوها"

    name = models.CharField("نام ویدئو", max_length=200)
    description = models.TextField("توضیحات ویدئو", blank=True)
    video = models.FileField(upload_to="video_uploaded/", null=True)

    def __str__(self):
        return self.name


class CommentOfVideos(models.Model):
    post = models.ForeignKey(Videos, on_delete=models.CASCADE, related_name='comment_Videos', verbose_name="نام ویدئو")
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
