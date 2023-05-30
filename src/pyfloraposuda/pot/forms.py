from django import forms
from .models import Pot

INPUT_CLASSES ='w-full py-4 px-6 rounded-xl border'

class EditPotForm(forms.ModelForm):
    """clasa za uređivanje posude

    Args:
        forms (django model): clasa za uređivanje posude
    """
    class Meta:
        model = Pot
        fields = {'name', 'plant'}
        widgets = {
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'plant': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),

        }

class NewPotForm(forms.ModelForm):
    """clasa za kreiranje posude

    Args:
        forms (django model): clasa za kreiranje posude
    """
    class Meta:
        model = Pot
        fields = {'name', 'plant'}
        widgets = {
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'plant': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
        }