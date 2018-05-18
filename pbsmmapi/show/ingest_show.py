from ..abstract.helpers import set_json_serialized_field

def process_show_record(obj, instance):
    
# These are the top-level fields - almost everything else is under attrs
    data = obj['data']
    attrs = data['attributes']
    links = obj['links']
    
#### UUID and updated_on
    instance.object_id = data.get('id', None)  # This should always be set.
    instance.updated_at = attrs.get('updated_at', None) # timestamp of the record in the API
    instance.api_endpoint = links.get('self', None) # URL of the request
    
#### Title, Sortable Ttile, and Slug
    instance.title = attrs.get('title', None)
    instance.title_sortable = attrs.get('title_sortable', None)
    instance.slug = attrs.get('slug', None)
    instance.json = obj
    return instance