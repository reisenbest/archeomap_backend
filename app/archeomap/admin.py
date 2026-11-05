from django.contrib import admin
from .models.models import *
from .forms import MonumentsAdminForm
import json
from django.urls import reverse
from django.templatetags.static import static
# Register your models here.


@admin.register(Monuments)
class MonumentsAdmin(admin.ModelAdmin):
    form = MonumentsAdminForm
    list_display = ('id', 'title', 'name', 'latitude', 'longitude', 'visible')
    list_filter = ('visible', 'title')
    list_editable = ('visible',)
    search_fields = ('title', 'name', 'description', 'title')
    list_per_page = 20

    filter_horizontal = (
        'dating',
        'classification_category',
        'custom_category',
        'research_years',
        'authors',
        'organizations',
    )
    
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)

        # Django может создавать служебную форму без этого поля.
        if not any(
            name in form.base_fields
            for name in ("description", "article")
        ):
            return form

        images = []

        if obj is not None:
            for image in obj.images.all().order_by("id"):
                if not image.image:
                    continue

                images.append({
                    "id": str(image.pk),
                    "caption": image.description or "",
                    "url": request.build_absolute_uri(
                        image.image.url
                    ),
                })

        

        # Данные для нашей кнопки «Карусель».
        # Django безопасно экранирует значение HTML-атрибута.
        for field_name in ("description", "article"):
            if field_name not in form.base_fields:
                continue

            widget = form.base_fields[field_name].widget
            widget.attrs["data-glossary-url"] = reverse( "glossary:term-list")
            widget.attrs["data-carousel-images"] = json.dumps(
                images,
                ensure_ascii=False,
            )

            widget.mce_attrs.update({
                "image_list": [
                    {
                        "title": (
                            image["caption"]
                            or f'Фотография № {image["id"]}'
                        ),
                        "value": image["url"],
                    }
                    for image in images
                ],
                "image_caption": True,
                "image_uploadtab": False,
                "convert_urls": False,
                "external_plugins": {
                            "monument_carousel": static(
                                "monument-carousel.js"
                            ),
                            "term_explanation": static(
                                "term-explanation.js"
                            ),
                        },
    
                       })

        return form

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

@admin.register(ExcavationsSquare)
class ExcavationsSquareAdmin(admin.ModelAdmin):
    list_display = ('id', 'monument')
    search_fields = ('monument__title', 'description')
    list_per_page = 20