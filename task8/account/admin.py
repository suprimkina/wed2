from django.contrib import admin

from .models import CustomUser, Profile


# Register your models here.
@admin.register(CustomUser)
class ProgLangAdmin(admin.ModelAdmin):
    pass


@admin.register(Profile)
class Admin(admin.ModelAdmin):
    pass
