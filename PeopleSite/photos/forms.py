from django import forms

from PeopleSite.photos.models import Photo


class PhotoCreateForm(forms.ModelForm):
    class Meta:
        fields = ('photo', 'description')
        model = Photo
