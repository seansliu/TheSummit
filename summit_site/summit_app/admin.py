from django.contrib import admin
from summit_app.models import Question, Comment


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 2


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Username', {'fields': ['author']}),
        ('Question', {'fields': ['question_text']}),
        ('Date Information', {
            'fields': ['pub_date'],
            'classes': ['collapse']
            }),
        ('Occupation', {'fields': ['occupation']})
    ]
    inlines = [CommentInline]
    list_display = ('question_text', 'author', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)
