from django import forms
from tinymce.widgets import TinyMCE

from .models.models import Monuments


class MonumentsAdminForm(forms.ModelForm):
    class Meta:
        model = Monuments
        fields = "__all__"
        widgets = {
            "description": TinyMCE(),
            "article": TinyMCE(),
        }