from ..abstract.helpers import set_json_serialized_field

### THIS IS THE INGEST SCRIPT FOR ASSET RECORDS

# This just makes nice serialized JSON content fragments from the API record's JSON content.
# It's a dirty way to avoid having to create ancillary tables with foreign keys back to objects.
# For example, let's say there's a field that shows all of the available languages for an object; do you
# REALLY want to have N records for EACH object that just says object #1234 is in English/Spanish?
# No - of course you don't.   So instead have a SINGLE simple field that has the value of, e.g., 
# ['en', 'es'] that you can de-serialize as necessary with the appropriate tests.
#
# I find that this works GREAT with model properties.  Using the above example you could quickly create
# a "is_spanish_available" property in a few lines:
#
#    def is_spanish_available(self):
#        langs = json.loads(self.languages)
#        return 'en' in lange
#    is_spanish_available = property(is_spanish_available)
#
# Wow - that was simple!
# RAD - 6 Feb 2018

def process_asset_record(obj, instance, origin=None):
# Here is where all the scraping of the Asset record is done
#
# These are the top-level fields - almost everything else is under attrs
    #attrs = obj['attributes']
    #links = obj['links']
    
    attrs = obj.get('attributes')
    links = obj.get('links')
    
#### UUID and updated_on
    instance.object_id = obj.get('id', None) # we want this because sometimes we've looked it up via COVE ID, not knowing the UUID
    
    instance.updated_at = attrs.get('updated_at', None)  # timestamp of the record in the API
    instance.api_endpoint = links.get('self', None) # the URL of the request

#### Title, Sortable Title, and Slug
    instance.title = attrs.get('title', None)
    instance.title_sortable = attrs.get('title_sortable', None)
    instance.slug = attrs.get('slug', None)
    instance.legacy_tp_media_id = attrs.get('legacy_tp_media_id', None)
    
    return instance

