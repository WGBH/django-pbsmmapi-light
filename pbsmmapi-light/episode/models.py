from django.db import models
from ..abstract.models import PBSMMLightObject

class PBSMMLightEpisode(PBSMMLightObject):
    pass
    
    class Meta:
        db_table = 'episode'
        app_label = 'pbsmmapi'