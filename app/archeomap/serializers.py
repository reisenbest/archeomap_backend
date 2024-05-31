# serializers.py
from rest_framework import serializers
from archeomap.models.models import *



class ImagesOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = ('image', 'description', 'link')

class MonumentsPublicOutputSerializer(serializers.ModelSerializer):
    dating = serializers.SerializerMethodField()
    classification_category = serializers.SerializerMethodField()
    custom_category = serializers.SerializerMethodField()
    research_years = serializers.SerializerMethodField()    
    authors = serializers.SerializerMethodField()
    organizations = serializers.SerializerMethodField()
    sources = serializers.SerializerMethodField()
    content = serializers.SerializerMethodField()
    excavations_square = serializers.SerializerMethodField()
    images = ImagesOutputSerializer(many=True)
    
    latitude = serializers.ModelField(model_field=Monuments._meta.get_field('latitude'))
    longitude = serializers.ModelField(model_field=Monuments._meta.get_field('longitude'))
    
    class Meta:
        model = Monuments
        fields = ('id', 'title', 'name', 'description', 'landmark', 'address', 
                  'slug', 'visible', 'latitude', 'longitude','dating', 'classification_category', 
                  'custom_category', 'research_years', 'authors', 'organizations',
                   'sources','content', 'images', 'excavations_square')
    
    def get_dating(self, monument_instance):
        """
        функция для оборачивания данный в нужный формат для вывода по гет запросу 
        берем monument_instance, Обращаемся к полю m2m (датировка в данном случае)
        берем все объекты dating связанные с переданным monument_instance
        получаем саму дату dating_value
        кладем ее в список

        Args:
            monument_instance (database objects): конкретный памятник, перебираем все памятники в представлении
            и для каждого вызываем эту функцию

        Returns:
            list: элементы списка - датировки, относящиеся к каждому конкретному памятнику
        """
        dating = [dating.dating_value for dating in monument_instance.dating.all()]
        return dating

    def get_classification_category(self, monument_instance) -> list:
        category = [classification.classification_category_value for classification in monument_instance.classification_category.all()]
        return category

    def get_custom_category(self, monument_instance) -> list:
        custom_category = [custom_category.custom_category_value for custom_category in monument_instance.custom_category.all()]
        return custom_category
    
    def get_research_years(self, monument_instance) -> list:
        research_years = [year_instance.year for year_instance in monument_instance.research_years.all()]
        return research_years

    def get_authors(self, monument_instance) -> list:
        authors = [author.author for author in monument_instance.authors.all()]
        return authors
    
    def get_organizations(self, monument_instance) -> list:
        organizations = [organization.organization for organization in monument_instance.organizations.all()]
        return organizations
    
    def get_sources(self, monument_instance) -> dict:
        sources = {source.title: source.link for source in monument_instance.sources.all()}
        return sources
    
    def get_content(self, monument_instance) -> dict:
        content = {content.title: content.link for content in monument_instance.content.all()}
        return content
    
    def get_excavations_square(self, monument_instance):
         return [excavation.excavation_square for excavation in monument_instance.excavations_square.all()]
    