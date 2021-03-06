from ..api.api import get_PBSMM_record
from ..api.helpers import check_pagination

from ..season.models import PBSMMSeason
from ..season.ingest_season import process_season_record

from ..special.models import PBSMMSpecial
from ..special.ingest_special import process_special_record

def process_seasons(endpoint, this_show): 
    # OK - get the record from the API
    keep_going = True
    while keep_going:
        (status, json) = get_PBSMM_record(endpoint) # this is the "Seasons" endpoint for the show
        season_list = json['data']        
        also_process_episodes = this_show.ingest_episodes
    
        for item in season_list:
            attrs = item.get('attributes')
            links = item.get('links')
            object_id = item.get('id')
            try:
                instance = PBSMMSeason.objects.get(object_id=object_id)
            except PBSMMSeason.DoesNotExist:
                instance = PBSMMSeason()
            
            instance = process_season_record(item, instance, origin='show')
            instance.show = this_show
            instance.ingest_on_save = True
        
            if also_process_episodes:
                instance.ingest_episodes = True
            
            instance.save()
        
        (keep_going, endpoint) = check_pagination(json)
         
    return

def process_specials(endpoint, this_show): 
    # OK - get the record from the API
    
    keep_going = True
    while keep_going:
        (status, json) = get_PBSMM_record(endpoint) # this is the "Seasons" endpoint for the show
        data = json['data']

        for item in data:
            attrs = item.get('attributes')
            links = item.get('links')
            object_id = item.get('id')
        
            try:
                instance = PBSMMSpecial.objects.get(object_id=object_id)
            except PBSMMSpecial.DoesNotExist:
                instance = PBSMMSpecial()
            
            instance = process_special_record(item, instance, origin='show')

            instance.show = this_show
            instance.ingest_on_save = True
        
            # This needs to be here because otherwise it never updates...
            instance.save()
        
        (keep_going, endpoint) = check_pagination(json)
        
    return