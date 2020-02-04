from django.forms import ModelForm

from link.models import Link


class LinkForm(ModelForm):
    class Meta:
        model = Link
        fields = ['key', 'link']
