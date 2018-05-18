from ..abstract.helpers import set_json_serialized_field
def process_season_record(obj, instance, origin='season'):
    
# These are the top-level fields - almost everything else is under attrs
    if 'attributes' not in obj.keys():
        attrs = obj['data']['attributes']
    else:
        attrs = obj['attributes']
        
    links = obj['links']

#### UUID and updated_on
    if 'id' in obj.keys():
        instance.object_id = obj.get('id', None)  # This should always be set.
    else:
        instance.object_id = obj['data'].get('id')
        
    instance.updated_at = attrs.get('updated_at', None) # timestamp of the record in the API
    instance.api_endpoint = links.get('self', None) # URL of the request

#### Title, Sortable Ttile, and Slug
    instance.title = attrs.get('title', None)
    instance.title_sortable = attrs.get('title_sortable', None)
    #instance.slug = attrs.get('slug', None)
    instance.ordinal = attrs.get('ordinal', None)
    instance.json = obj
    return instance