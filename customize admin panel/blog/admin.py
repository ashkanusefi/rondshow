from django.contrib import admin, messages
from .models import Articles, Category
from django.utils.translation import ngettext

admin.site.site_header = 'مدیریت BARMAN'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['position', 'title', 'parent', 'status']
    list_filter = (['status'])
    list_editable = ['status']
    search_fields = ['title']
    prepopulated_fields = {'slug': ('title',)}

    actions = ['make_active', 'make_deactivate']

    @admin.action(description='فعال کردن دسته بندی های انتخاب شده')
    def make_active(self, request, queryset):
        updated = queryset.update(status=True)
        self.message_user(request, ngettext(
            '%d دسته بندی با موفقیت فعال شد',
            '%d دسته بندی با موفقیت فعال شدند',
            updated,
        ) % updated, messages.SUCCESS)

    @admin.action(description='غیرفعال کردن دسته بندی های انتخاب شده')
    def make_deactivate(self, request, queryset):
        updated = queryset.update(status=False)
        self.message_user(request, ngettext(
            '%d دسته بندی با موفقیت غیرفعال شد',
            '%d دسته بندی با موفقیت غیرفعال شدند',
            updated,
        ) % updated, messages.SUCCESS)


admin.site.register(Category, CategoryAdmin)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['thumbnail_tag', 'title', 'jpublish', 'author', 'is_special', 'category_to_str', 'status']
    list_filter = ['publish', 'status', 'author']
    list_editable = ['status']
    search_fields = ['title', 'description']
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['status', '-publish']
    actions = ['make_published', 'make_draft']

    @admin.action(description='انتشار مقالات انتخاب شده')
    def make_published(self, request, queryset):
        updated = queryset.update(status='p')
        self.message_user(request, ngettext(
            '%d مقاله با موفقیت منتشر شد',
            '%d مقاله با موفقیت منتشر شدند',
            updated,
        ) % updated, messages.SUCCESS)

    @admin.action(description='پیش نویس شدن مقالات انتخاب شده')
    def make_draft(self, request, queryset):
        updated = queryset.update(status='d')
        self.message_user(request, ngettext(
            '%d مقاله با موفقیت به پیش نویس تغییر یافت',
            '%d مقاله با موفقیت به پیش نویس تغییر یافتند',
            updated,
        ) % updated, messages.SUCCESS)


admin.site.register(Articles, ArticleAdmin)
