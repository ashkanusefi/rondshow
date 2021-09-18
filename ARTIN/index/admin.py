from django.contrib import admin

from index.models import Questions, Contactform, Main_pic,Advisor


class MyAdmin(admin.ModelAdmin):
    def has_add_permission(self, request, obj=None):
        return False


admin.site.register(Main_pic)
admin.site.register(Questions)
admin.site.register(Advisor)
admin.site.register(Contactform, MyAdmin)
