from django.db import models
from ..abstract.models import PBSMMLightObject

class PBSMMLightRemoteAsset(PBSMMLightObject):
    pass
    
    class Meta:
        db_table = 'remoteasset'
        app_label = 'pbsmmapi'