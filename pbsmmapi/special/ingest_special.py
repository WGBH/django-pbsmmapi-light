from ..abstract.helpers import set_json_serialized_field

def process_special_record(obj, instance, origin='native'):
    
# These are the top-level fields - almost everything else is under attrs
    if 'attributes' not in obj.keys():
        return instance
    else:
        attrs = obj['attributes']
    if 'links' not in obj.keys():
        return instance
    else:
        links = obj['links']
    
#### UUID and updated_on
    instance.object_id = obj.get('id', None)  # This should always be set.
    instance.updated_at = attrs.get('updated_at', None) # timestamp of the record in the API
    instance.api_endpoint = links.get('self', None) # URL of the request
    
#### Title, Sortable Ttile, and Slug
    instance.title = attrs.get('title', None)
    instance.title_sortable = attrs.get('title_sortable', None)
    instance.slug = attrs.get('slug', None)

#### Unprocessed - store as JSON fragments
    instance.links = set_json_serialized_field(attrs, 'links', default=None)
    instance.json = obj

    return instance