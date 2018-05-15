from django.db import models
from ..abstract.models import PBSMMLightSeasonObject

class PBSMMLightSeason(PBSMMLightSeasonObject):
    pass
    
    class Meta:
        db_table = 'season'
        app_label = 'pbsmmapi-light'