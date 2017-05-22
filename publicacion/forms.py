from django import forms
from .models import Entrada

class PostForm(forms.ModelForm):

    class Meta:
        model = Entrada
        fields = ['titulo', 'contenido', 'imagen', 'email', 'number']

        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'input'}),
            'contenido': forms.Textarea()
	}