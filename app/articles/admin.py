from django.contrib import admin
from .models import (
    Articles,
    Categories,
    Tags,
    Authors,
    ArticleImages,
    ArticlePreviewImage,
)
from .forms import ArticlesAdminForm
import json

from django.urls import reverse
from django.templatetags.static import static


# Register your models here.

class ArticleImagesInline(admin.TabularInline):
    model = ArticleImages
    extra = 1
    fields = ('image', 'description', 'link')


class ArticlePreviewImageInline(admin.StackedInline):
    model = ArticlePreviewImage
    extra = 1
    max_num = 1
    fields = ('image',)

@admin.register(Articles)
class ArticlesAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'is_published',
        'created_at',
        'updated_at',
    )

    search_fields = ('title', 'preview_text')

    list_filter = ('is_published',)

    prepopulated_fields = {'slug': ('title',)}

    readonly_fields = ('created_at', 'updated_at')

    filter_horizontal = ('categories', 'tags', 'authors')

    inlines = (
        ArticlePreviewImageInline,
        ArticleImagesInline,
    )

    form = ArticlesAdminForm

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)

        if 'main_text' not in form.base_fields:
            return form

        images = []

        if obj is not None:
            for image in obj.images.all().order_by('id'):
                if not image.image:
                    continue

                images.append({
                    'id': str(image.pk),
                    'caption': image.description or '',
                    'url': request.build_absolute_uri(image.image.url),
                })

        widget = form.base_fields['main_text'].widget

        widget.attrs['data-glossary-url'] = reverse(
            'glossary:term-list'
        )

        widget.attrs['data-carousel-images'] = json.dumps(
            images,
            ensure_ascii=False,
        )

        widget.mce_attrs.update({
            'image_list': [
                {
                    'title': (
                        image['caption']
                        or f"Фотография № {image['id']}"
                    ),
                    'value': image['url'],
                }
                for image in images
            ],
            'image_caption': True,
            'image_uploadtab': False,
            'convert_urls': False,
            'external_plugins': {
                'monument_carousel': static('monument-carousel.js'),
                'term_explanation': static('term-explanation.js'),
            },
        })

        return form

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    search_fields = ('article_category_value',)


@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    search_fields = ('article_tag_value',)


@admin.register(Authors)
class AuthorsAdmin(admin.ModelAdmin):
    search_fields = ('author',)


