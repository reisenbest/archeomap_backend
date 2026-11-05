from django.contrib import admin

from .models import GlossaryTerm, GlossaryImages
import json

from django.templatetags.static import static

from .forms import GlossaryTermAdminForm

class GlossaryImagesInline(admin.TabularInline):
    model = GlossaryImages
    extra = 1
    fields = ("image", "description", "link")


@admin.register(GlossaryTerm)
class GlossaryTermAdmin(admin.ModelAdmin):

    form = GlossaryTermAdminForm
    
    list_display = (
        "title",
        "slug",
        "is_published",
        "updated_at",
    )

    search_fields = ("title", "short_definition")
    list_filter = ("is_published",)
    prepopulated_fields = {"slug": ("title",)}
    readonly_fields = ("created_at", "updated_at")

    fields = (
        "title",
        "slug",
        "short_definition",
        "description",
        "is_published",
        "created_at",
        "updated_at",
    )

    inlines = [GlossaryImagesInline]
    
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)

        if "description" not in form.base_fields:
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

        widget = form.base_fields["description"].widget

        widget.attrs["data-carousel-images"] = json.dumps(
            images,
            ensure_ascii=False,
        )

        widget.mce_attrs.update({
            "image_list": [
                {
                    "title": (
                        image["caption"]
                        or f'Изображение № {image["id"]}'
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
            },
        })

        return form

