from django.forms import ModelForm

from .models import PBSMMShow

class PBSMMShowCreateForm(ModelForm):

    class Meta:
        model = PBSMMShow
        fields = (
            'slug', 
            'ingest_seasons', 'ingest_specials', 
        )

class PBSMMShowEditForm(ModelForm):

    class Meta:
        model = PBSMMShow
        exclude = []
