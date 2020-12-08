from django.contrib import admin

from .models import Note


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'creation_date', 'update_date')
    fields = ('title', 'text', )
    readonly_fields = ('creation_date', 'update_date')