from django import forms
from tinymce.widgets import TinyMCE

from .models import GlossaryTerm

class GlossaryTermAdminForm(forms.ModelForm):
    class Meta:
        model = GlossaryTerm
        fields = "__all__"
        widgets = {
            "short_definition": TinyMCE(
                mce_attrs={
                    "height": 250,
                    "menubar": False,
                    "plugins": "lists link",
                    "toolbar": (
                        "undo redo | bold italic | "
                        "bullist numlist | link | removeformat"
                    ),
                }
            ),
            "description": TinyMCE(),
        }