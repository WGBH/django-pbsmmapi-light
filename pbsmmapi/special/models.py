from django.db import models
from ..abstract.models import PBSMMLightObject

class PBSMMLightSpecial(PBSMMLightObject):
    pass
    
    class Meta:
        db_table = 'special'
        app_label = 'pbsmmapi'