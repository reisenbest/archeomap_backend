def image_upload_to(instance, filename) -> str:
    """Автоматическое создание пути для загрузки файла изображений
    путь формируется собственно слова - его слага

    Args:
        instance (): объект из таблицы Images
        filename (str): имя файла загружаемого 

    Returns:
        str: строка, определяющая путь для сохранения
    """
    return f"glossary/{instance.glossary_term.slug}/{filename}"



from django.utils.text import slugify
##№ функция для создания слага 
def make_slug(value):
    translit_dict = {
        'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'yo', 'ж': 'zh', 'з': 'z', 'и': 'i',
        'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't',
        'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'sch', 'ы': 'y', 'э': 'e', 'ю': 'yu',
        'я': 'ya', ' ': '-', '.': '', ',': '', '?': '', '!': '', ':': '', ';': '', '"': '', '(': '', ')': '', 
        '[': '', ']': '', '{': '', '}': '', '/': '-', '\\': '-', '-': '-', '_': '-'
    }

    value = str(value)
    # Преобразуем в транслит, заменяя буквы согласно словарю
    value = ''.join([translit_dict.get(char, char) for char in value.lower()])
    
    # Убираем лишние дефисы на границах
    return slugify(value)
