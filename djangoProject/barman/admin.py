from django.contrib import admin

from barman.models import Ab, Cont, Data_form


class MyAdmin(admin.ModelAdmin):
    # def has_add_permission(self, request, obj=None):
    #     return False
    def has_add_permission(self, request):
        return True

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(Ab, MyAdmin)
admin.site.register(Cont, MyAdmin)
admin.site.register(Data_form, MyAdmin)
