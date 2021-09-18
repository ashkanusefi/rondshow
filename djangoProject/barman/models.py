from django.db import models


class Ab(models.Model):
    class Meta:
        verbose_name = "درباره ما"
        verbose_name_plural = "درباره ما"

    name = "درباره ما"
    name_one = models.CharField("عنوان بخش اول", max_length=200, blank=True)
    section_one = models.TextField("توضیحات بخش اول", blank=True)
    name_two = models.CharField("عنوان بخش دوم", max_length=200, blank=True)
    section_two = models.TextField("توضیحات بخش دوم", blank=True)

    def __str__(self):
        return self.name


class Cont(models.Model):
    class Meta:
        verbose_name = "تماس با ما"
        verbose_name_plural = "تماس با ما"

    name = "تماس با ما"
    title = models.CharField("عنوان", max_length=500, blank=True)
    description = models.TextField("توضیح تماس با ما", blank=True)
    phone = models.CharField('شماره تماس اول', blank=True, max_length=22)
    instagram = models.CharField('اینستاگرام', blank=True, max_length=22)
    telegram = models.CharField('تلگرام', blank=True, max_length=22)
    address = models.TextField("ادرس")
    email = models.CharField('ایمیل', blank=True, max_length=50)

    def __str__(self):
        return self.name


class Data_form(models.Model):
    class Meta:
        verbose_name = "فرم دریافتی"
        verbose_name_plural = "فرم دریافتی"

    name = models.CharField("نام و نام خانوادگی", max_length=120)
    email = models.CharField("ایمیل", max_length=200)
    phone = models.CharField("شماره تلفن", max_length=20)
    description = models.TextField("پیغام شما", blank=True, null=True)

    def __str__(self):
        return self.name
