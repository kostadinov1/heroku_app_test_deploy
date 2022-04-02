from django.contrib import admin

# Register your models here.
from heroku_app.main.models import Note


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    pass