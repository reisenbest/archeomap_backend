from pathlib import Path
from uuid import uuid4


def article_image_upload_to(instance, filename):
    extension = Path(filename).suffix.lower()

    return f'articles/{instance.article_id}/{uuid4().hex}{extension}'


def article_preview_image_upload_to(instance, filename):
    extension = Path(filename).suffix.lower()

    return f'articles/preview_image/{instance.article_id}/{uuid4().hex}{extension}'