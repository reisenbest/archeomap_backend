from django.contrib import admin
from .models import MonumentTest

@admin.register(MonumentTest)
class MonumentTestAdmin(admin.ModelAdmin):
    list_display = ('title',)