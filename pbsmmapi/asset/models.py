from django.db import models
from ..abstract.models import PBSMMLightObject

class PBSMMLightAsset(PBSMMLightObject):
    pass
    
    class Meta:
        db_table = 'asset'
        app_label = 'pbsmmapi'