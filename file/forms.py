from django import forms

from file.models import File


class UploadFileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ('name', 'file', )
