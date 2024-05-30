from django.contrib import admin
from .models.models import Bibliography

# Register your models here.
@admin.register(Bibliography)
class BibliographyAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'source', 'publication_date', 'source_identificator', 
                    'main_category', 'sub_category', 'slug', 'visible')
    list_filter = ('visible','publication_date')
    list_editable = ('visible',)
    search_fields = ('title', 'source_identificator',
                     'main_category', 'sub_category','publication_date', 'source')
    list_per_page = 20
