from django.db import models
from ..abstract.models import PBSMMLightObject

class PBSMMLightFranchise(PBSMMLightObject):
    pass
    
    class Meta:
        db_table = 'franchise'
        app_label = 'pbsmmapi'