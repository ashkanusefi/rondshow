from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    class Meta:
        verbose_name = "نمایه کاربری"
        verbose_name_plural = "نمایه کاربری"

    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="حساب کاربری")
    mobile = models.CharField("شماره موبایل", max_length=11)
    MALE = 1
    FEMALE = 2
    GENDER_CHOICE = ((MALE, "مرد"), (FEMALE, "زن"))
    GENDER = models.IntegerField("نسیت", choices=GENDER_CHOICE, null=True, blank=True)
    birth_date = models.DateField("تاریخ تولد", null=True, blank=True)
    address = models.TextField("ادرس", null=True, blank=True)
    profile_image = models.ImageField("تصویر", upload_to="image_uploaded/", null=True, blank=True)

    def __str__(self):
        return self.user.get_full_name()
