
def pre_save_operation(instance):
    # If this is a new record, then someone has started it in the Admin using EITHER a legacy COVE ID
    # OR a PBSMM UUID.   Depending on which, the retrieval endpoint is slightly different, so this sets
    # the appropriate URL to access.
    if instance.pk is None: 
        if instance.object_id and instance.object_id.strip():
            url = __get_api_url('pbsmm', instance.object_id)
        else:
            if instance.legacy_tp_media_id:
                url = __get_api_url('cove', str(instance.legacy_tp_media_id))
            else:
                return # do nothing - can't get an ID to look up!
                
    # Otherwise, it's an existing record and the UUID should be used
    else: # Editing an existing  record  - do nothing if ingest_on_save is NOT checked!
        if not instance.ingest_on_save:
            return
        url = __get_api_url('pbsmm', instance.object_id)
    
    # OK - get the record from the API
    (status, json) = get_PBSMM_record(url)
    instance.last_api_status = status
    
    # Update this record's time stamp (the API has its own)
    instance.date_last_api_update = datetime.datetime.now()
    
    if status != 200:
        return 
        
    # Process the record (code is in ingest.py)
    instance = process_asset_record(json, instance)
    
    # continue saving, but turn off the ingest_on_save flag
    instance.ingest_on_save = False # otherwise we could end up in an infinite loop!
    
    # We're done here - continue with the save() operation 
    return
    