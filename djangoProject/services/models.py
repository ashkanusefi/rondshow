from django.db import models


class Service(models.Model):
    class Meta:
        verbose_name = "خدمات"
        verbose_name_plural = "خدمات"

    title = models.CharField("عنوان خدمات", max_length=200)
    description = models.TextField("تومضیحات")
    image = models.ImageField("تصویر خدمات", upload_to="video_uploaded/", blank=True)
    film = models.FileField("ویدئو خدمات", upload_to="video_uploaded/", blank=True)

    def __str__(self):
        return self.title


class Sub(models.Model):
    class Meta:
        verbose_name = "زیرخدمات"
        verbose_name_plural = "زیرخدمات"

    title = models.CharField("عنوان پروژه", max_length=200)
    head = models.ForeignKey("Service", verbose_name="نام سردسته", on_delete=models.CASCADE)
    link = models.CharField("لینک پروژه", max_length=300)
    text = models.TextField("توضیحات پروژه")
    image = models.ImageField("تصویر پروژه", upload_to="image_uploaded", blank=True)
    film = models.FileField("فیلم پروژه", upload_to="video_uploaded", blank=True)

    def __str__(self):
        return self.title
