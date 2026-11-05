from rest_framework import serializers

from .models import (
    Articles,
    Categories,
    Tags,
    Authors,
    ArticleImages,
    ArticlePreviewImage,
)


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ('id', 'article_category_value')


class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = ('id', 'article_tag_value')


class AuthorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Authors
        fields = ('id', 'author')


class ArticleImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleImages
        fields = ('id', 'image', 'description', 'link')


class ArticlePreviewImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticlePreviewImage
        fields = ('id', 'image')


class ArticlesListSerializer(serializers.ModelSerializer):
    categories = CategoriesSerializer(many=True, read_only=True)
    tags = TagsSerializer(many=True, read_only=True)
    authors = AuthorsSerializer(many=True, read_only=True)

    preview_image = ArticlePreviewImageSerializer(
        read_only=True,
        allow_null=True,
    )

    class Meta:
        model = Articles
        fields = (
            'id',
            'title',
            'slug',
            'preview_text',
            'preview_image',
            'categories',
            'tags',
            'authors',
            'created_at',
            'updated_at',
        )


class ArticlesDetailSerializer(ArticlesListSerializer):
    images = ArticleImagesSerializer(
        many=True,
        read_only=True,
    )

    class Meta(ArticlesListSerializer.Meta):
        fields = ArticlesListSerializer.Meta.fields + (
            'main_text',
            'images',
        )