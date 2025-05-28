from django.contrib import admin

from .models import ProgLang, Application


@admin.register(ProgLang)
class ProgLangAdmin(admin.ModelAdmin):
    list_display = ('id', 'prog_lang_name')

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    pass

