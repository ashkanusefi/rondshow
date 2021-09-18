from django.db import models


class Menu(models.Model):
    parent = models.ForeignKey("Menu", null=True, on_delete=models.SET_NULL, related_name="sub_menus")
    name = models.CharField(max_length=200, blank=False, null=False)

    def __str__(self):
        return self.name
