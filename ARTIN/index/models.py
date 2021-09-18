from django.db import models


class Main_pic(models.Model):
    class Meta:
        verbose_name = "عکس اصلی"
        verbose_name_plural = "عکس اصلی"

    name = models.CharField("نام عکس", max_length=200)
    picture = models.ImageField("عکس", upload_to="images/")
    text = models.CharField("نوشته عکس", max_length=300)

    def __str__(self):
        return self.name


class Questions(models.Model):
    class Meta:
        verbose_name = "سوال متدواول"
        verbose_name_plural = "سوال متداول"

    name = models.CharField("نام سوال", max_length=40)
    question = models.CharField("متن سوال", max_length=300)
    answer = models.TextField("پاسخ سوال")

    def __str__(self):
        return self.name


class Contactform(models.Model):
    class Meta:
        verbose_name = "فرم دریافتی"
        verbose_name_plural = "فرم دریافتی"

    name = models.CharField("نام و نام خانوادگی", max_length=120)
    email = models.CharField("ایمیل", max_length=200)
    subject = models.CharField("موضوع", max_length=500)
    phone = models.CharField("شماره تلفن", max_length=20)
    description = models.TextField("پیغام شما", blank=True, null=True)

    def __str__(self):
        return self.name


class Advisor(models.Model):
    class Meta:
        verbose_name = "کارمند"
        verbose_name_plural = "کارمند"

    name = models.CharField("نام و نام خانوادکی", max_length=200)
    job = models.CharField("شغل", max_length=200)
    description = models.TextField("توضیحات")
    picture = models.ImageField("تصویر کارمند", upload_to="images")

    def __str__(self):
        return self.name
