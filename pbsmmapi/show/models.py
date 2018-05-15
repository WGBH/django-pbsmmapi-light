from django.db import models
from ..abstract.models import PBSMMLightObject

class PBSMMLightShow(PBSMMLightObject):
    pass
    
    class Meta:
        db_table = 'show'
        app_label = 'pbsmmapi'