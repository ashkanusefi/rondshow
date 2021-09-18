from django.contrib import admin

from news.models import Tag, News, Category

admin.site.site_header = "صفحه مدیریت ادمین"


class NewAdmin(admin.ModelAdmin):
    list_display = ['title', 'thumbnail', 'publish_date', 'name', 'tag_to_str']
    list_filter = ['name']
    search_fields = ['name', 'title', 'publish_date']
    ordering = ['-publish_date']

    def tag_to_str(self, obj):
        return ",".join([tag.tag for tag in obj.tag.all()])

    tag_to_str.short_description = "دسته بندی"


admin.site.register(News, NewAdmin)
admin.site.register(Category)
admin.site.register(Tag)
