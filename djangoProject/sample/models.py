from django.db import models


class Sample(models.Model):
    class Meta:
        verbose_name = "سر دسته نمونه کار"
        verbose_name_plural = "سر دسته نمونه کار"

    title = models.CharField("نام سردسته نمونه کار", max_length=200)
    description = models.TextField("توضیحات سردسته نمونه کار")
    image = models.ImageField("تصویر سردسته نمونه کار", upload_to="image_uploaded/", blank=True, null=True)

    def __str__(self):
        return self.title


class Subsample(models.Model):
    class Meta:
        verbose_name = " نمونه کار"
        verbose_name_plural = "نمونه کار"

    title = models.CharField("عنوان نمونه کار", max_length=200)
    head = models.ForeignKey("Sample", verbose_name="نام سردسته", on_delete=models.CASCADE)
    link = models.CharField("لینک نمونه کار", max_length=300)
    text = models.TextField("توضیحات نمونه کار")
    image = models.ImageField("تصویر نمونه کار", upload_to="image_uploaded", blank=True)

    def __str__(self):
        return self.title
