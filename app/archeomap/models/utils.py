def image_upload_to(instance, filename) -> str:
    """Автоматическое создание пути для загрузки файла изображений
    путь формируется из идентификатора памятника кастомного, первые 4 цифры + слаг

    Args:
        instance (): объект из таблицы Images
        filename (str): имя файла загружаемого 

    Returns:
        str: строка, определяющая путь для сохранения
    """
    identificator = str(instance.monument.title)[:4]
    monument = str(instance.monument.slug).replace(' ', '_') if instance.monument else 'unknown'
    return f'monuments/{identificator}_{monument}/{filename}'
