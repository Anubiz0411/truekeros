from django import forms
from .models import Album
from .models import AlbumImage


class UploadImageForm(forms.ModelForm):

    class Meta:
        model = AlbumImage
        fields = ['album', 'image']

class PostForm(forms.ModelForm):
 	class Meta:
 		model = Album
 		fields = ('title', 'text',)
