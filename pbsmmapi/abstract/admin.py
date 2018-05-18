from django.contrib import admin

class PBSMMAbstractAdmin(admin.ModelAdmin):
    
    def force_reingest(self, request, queryset):
        # queryset is the list of Asset items that were selected.
        for item in queryset:
            item.ingest_on_save = True
            # HOW DO I FIND OUT IF THE save() was successful?
            item.save()
    force_reingest.short_description = 'Reingest selected items.'
    
    def make_publicly_available(self, request, queryset):
        for item in queryset:
            item.publish_status = 1
            item.save()
    make_publicly_available.short_description = 'Take item LIVE (to the public)'
            
    def take_offline(self, request, queryset):
        for item in queryset:
            item.publish_status = 0
            item.save() 
    take_offline.short_description = 'Take item OFFLINE (admin only)'
            
    class Meta:
        abstract = True
        
    
def get_abstract_asset_table(object_list):
    out = "<table width=\"100%\" border=2>"
    out += "\n<tr><th>Title</th><th>API</th><th>Admin</th><th>Popup</th></tr>"
    for item in object_list:
        out += "\n<tr>"
        out += "\n\t<td>%s</td>" % item.title
        out += "\n\t<td><a href=\"%s\" target=\"_new\">API</a></td>" % item.api_endpoint
        out += "\n\t<td><a href=\"/admin/episode/pbsmmepisodeasset/%d/change/\" target=\"_new\">Admin</a></td>" % item.id
        out += "\n\t<td>(soon)</td>"
        out += "\n</tr>"
    out += "\n</table>"
    return out