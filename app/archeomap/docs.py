from drf_spectacular.utils import extend_schema, extend_schema_serializer, OpenApiExample
from .serializers import MonumentsPublicOutputSerializer


get_monuments__public_scheme = extend_schema(
    description="Получение списка всех памятников для их отрисовки на карте и размещении информации в popup'e",
    summary="Получение списка всех памятников для их отрисовки на карте и размещении информации в popup'e",
    tags=['monuments', ],
    request=MonumentsPublicOutputSerializer,
    responses={200: MonumentsPublicOutputSerializer(many=True)},
    examples=[
         OpenApiExample(
            'Пример отдаваемых данных о памятнике 1',
            summary='Отдаваемые данные о памятнике',
            description='Включены все поля. m2m поля отдаются списком значений',
            value={
                     
                      "id": 0,
                      "title": "string",
                      "name": "string",
                      "description": "string",
                      "landmark": "string",
                      "address": "string",
                      "slug": "string",
                      "visible": 'true',
                      "latitude": 27.023222,
                      "longitude": 72.92313,
                      "dating": "string",
                      "classification_category": [
                        "string"
                      ],
                      "custom_category": [
                        "string"
                      ],
                      "research_years": [
                        "string"
                      ],
                      "authors": [
                        "string"
                      ],
                      "organizations": [
                        "string"
                      ],
                      "sources": [
                        "string"
                      ],
                      "content": [
                        "string"
                      ],
                      "images": [
                        {
                          "image": "string",
                          "description": "string"
                        }
                      ]
                                   
            },
            response_only=True, 
        ),
    ]
)
