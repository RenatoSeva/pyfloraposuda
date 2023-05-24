from django import forms
from .models import Pot

INPUT_CLASSES ='w-full py-4 px-6 rounded-xl border'

class EditPotForm(forms.ModelForm):
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