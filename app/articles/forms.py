from django import forms
from tinymce.widgets import TinyMCE

from .models import Articles


class ArticlesAdminForm(forms.ModelForm):
    class Meta:
        model = Articles
        fields = '__all__'
        widgets = {
            'main_text': TinyMCE(),
        }