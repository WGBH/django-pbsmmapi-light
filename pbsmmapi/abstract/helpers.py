import json

def set_json_serialized_field(attrs, field, default=None):
# Return a JSON serialized field, but don't send back [] or {} or '' (return default which default to None)
    val = attrs.get(field, default)
    if val:
        return json.dumps(val)
    else:
        return default
        
    