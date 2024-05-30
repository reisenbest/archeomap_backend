from django.contrib import admin
from .models.models import *
# Register your models here.


@admin.register(Monuments)
class MonumentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'name', 'latitude', 'longitude', 'visible')
    list_filter = ('visible', 'title')
    list_editable = ('visible',)
    search_fields = ('title', 'name', 'description', 'title')
    list_per_page = 20


@admin.register(Dating)
class DatingAdmin(admin.ModelAdmin):
    list_display = ('id', 'dating_value')
    search_fields = ('dating_value',)
    list_per_page = 20


@admin.register(Classification)
class ClassificationAdmin(admin.ModelAdmin):
    list_display = ('id', 'classification_category_value')
    search_fields = ('classification_category_value',)
    list_per_page = 20


@admin.register(CustomCategory)
class CustomCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'custom_category_value')
    search_fields = ('custom_category_value',)
    list_per_page = 20


@admin.register(ResearchYears)
class ResearchYearsAdmin(admin.ModelAdmin):
    list_display = ('id', 'year')
    search_fields = ('year',)
    list_per_page = 20


@admin.register(Authors)
class AuthorsAdmin(admin.ModelAdmin):
    list_display = ('id', 'author')
    search_fields = ('author',)
    list_per_page = 20


@admin.register(Organizations)
class OrganizationsAdmin(admin.ModelAdmin):
    list_display = ('id', 'organization')
    search_fields = ('organization',)
    list_per_page = 20


@admin.register(Sources)
class SourcesAdmin(admin.ModelAdmin):
    list_display = ('id', 'monument', 'title', 'link')
    search_fields = ('monument',)
    list_per_page = 20


@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ('id', 'monument', 'title', 'link')
    search_fields = ('monument',)
    list_per_page = 20


@admin.register(Images)
class ImagesAdmin(admin.ModelAdmin):
    list_display = ('id', 'monument', 'image', 'description', 'link')
    search_fields = ('monument__title', 'description')
    list_per_page = 20
