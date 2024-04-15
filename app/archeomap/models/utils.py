def image_upload_to(instance, filename):
    """

    :param instance: объект бд
    :param filename: имя загружаемого изображения
    :return: корректный путь куда нужно загрузить файл выбранный
    """
    monument = str(instance.monument).replace(' ', '_') if instance.monument else 'unknown'
    return f'monuments/{monument}/{filename}'
