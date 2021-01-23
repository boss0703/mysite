from django import forms

from .models import ImageFile


class DiscriminationForm(forms.ModelForm):
    class Meta:
        model = ImageFile
        fields = ('titlefield', 'filefield', )
