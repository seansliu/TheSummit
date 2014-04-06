from django.contrib import admin
from summit_app.models import Content


class ContentInline(admin.TabularInline):
    model = Content
    fk_name = 'parent_question'
    extra = 2


class ContentAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Username', {'fields': ['author']}),
        ('Content', {'fields': ['text']}),
        ('Date Information', {
            'fields': ['pub_date'],
            'classes': ['collapse']
            }),
    ]

    inlines = [ContentInline]
    list_display = ('text', 'author', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['text']

admin.site.register(Content, ContentAdmin)
