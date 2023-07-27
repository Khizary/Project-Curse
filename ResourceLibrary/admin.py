from django.contrib import admin
from .models import Entry, Subject, Level, Comment

class EntryAdmin(admin.ModelAdmin):
    list_display = ('name', 'restype', 'description','created_on','author')
    list_filter = ("created_on",)
    search_fields = ['name', 'description']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Entry, EntryAdmin)
admin.site.register(Subject)
admin.site.register(Level)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'entry', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)