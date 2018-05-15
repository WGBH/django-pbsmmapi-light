from django.db import models
from .abstract_models import PBSMMLightObject, PBSMMLightShowObject

class PBSMMLightAsset(PBSMMLightObject):
    pass
    
class PBSMMLightCollection(PBSMMLightObject):
    pass
    
class PBSMMLightEpisode(PBSMMLightObject):
    pass
    
class PBSMMLightFranchise(PBSMMLightObject):
    pass
    
class PBSMMLightRemoteAsset(PBSMMLightObject):
    pass
    
class PBSMMLightSeason(PBSMMLightShowObject):
    pass
    
class PBSMMLightShow(PBSMMLightObject):
    pass
    
class PBSMMLightSpecial(PBSMMLightObject):
    pass
    
