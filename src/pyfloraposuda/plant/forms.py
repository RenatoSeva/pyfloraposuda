from django import forms
from .models import Plant

INPUT_CLASSES ='w-full py-4 px-6 rounded-xl border'

class EditPlantForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = {'name', 'image', 'humidity', 'brightness', 'temperature', 'substrate'}
        widgets = {
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            }),
            'humidity': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'brightness': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'temperature': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'substrate': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            })

        }

class NewPlantForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = {'name', 'image', 'humidity', 'brightness', 'temperature', 'substrate'}
        widgets = {
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            }),
            'humidity': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'brightness': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'temperature': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'substrate': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            })

        }