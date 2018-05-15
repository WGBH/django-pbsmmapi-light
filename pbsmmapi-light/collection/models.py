from django.db import models
from ..abstract.models import PBSMMLightObject

class PBSMMLightCollection(PBSMMLightObject):
    pass
    
    class Meta:
        db_table = 'collection'
        app_label = 'pbsmmapi'