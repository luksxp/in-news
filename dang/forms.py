from django.forms import ModelForm

from dang.models import Link

class AddLinkModelForm(ModelForm):
    class Meta:
        model = Link
        