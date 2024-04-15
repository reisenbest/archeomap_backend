# serializers.py
from rest_framework import serializers
from .models.models import *

class TestCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TestCategory
        fields = ['category']

class TestModelSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField(many=True)

    class Meta:
        model = TestModel
        fields = ['name', 'latitude', 'longitude', 'category']

class ImagesSerializer(serializers.ModelSerializer):
    # image = serializers.SerializerMethodField()

    class Meta:
        model = Images
        fields = ('monument', 'image', 'description')

class MonumentsSerializer(serializers.ModelSerializer):
    sources = serializers.SerializerMethodField()
    content = serializers.SerializerMethodField()
    dating = serializers.SerializerMethodField()
    classification_category = serializers.SerializerMethodField()
    custom_category = serializers.SerializerMethodField()
    research_years = serializers.SerializerMethodField()
    authors = serializers.SerializerMethodField()
    organizations = serializers.SerializerMethodField()

    class Meta:
        model = Monuments
        fields = '__all__'

    def get_sources(self, obj):
        return [source.title for source in obj.sources.all()]

    def get_content(self, obj):
        return [{'title':content.title, 'link':content.link} for content in obj.content.all()]

    def get_dating(self, obj):
        return [dating.dating_value for dating in obj.dating.all()]

    def get_classification_category(self, obj):
        return [category.classification_category_value for category in obj.classification_category.all()]

    def get_custom_category(self, obj):
        return [category.custom_category_value for category in obj.custom_category.all()]

    def get_research_years(self, obj):
        return [year.year for year in obj.research_years.all()]

    def get_authors(self, obj):
        return [author.author for author in obj.authors.all()]

    def get_organizations(self, obj):
        return [organization.organization for organization in obj.organizations.all()]