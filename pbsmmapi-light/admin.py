from django.contrib import admin

from .models import PBSMMLightAsset, PBSMMLightEpisode, PBSMMLightSeason, PBSMMLightShow, PBSMMLightSpecial
    #PBSMMLightCollection,\
    #PBSMMLightFranchise,\
    #PBSMMLightRemoteAsset,\
    
global_readonly_fields = ['title', 'link_to_api_record', 'object_id', 'date_created', 'date_last_api_update', 'last_api_status']

class PBSMMLightAssetAdmin(admin.ModelAdmin):
    readonly_fields = global_readonly_fields
    
#class PBSMMLightCollectionAdmin(admin.ModelAdmin):
#   readonly_fields = global_readonly_fields
    
class PBSMMLightEpisodeAdmin(admin.ModelAdmin):
    readonly_fields = global_readonly_fields
    
#class PBSMMLightFranchiseAdmin(admin.ModelAdmin):
#   readonly_fields = global_readonly_fields
    
#class PBSMMLightRemoteAssetAdmin(admin.ModelAdmin):
#   readonly_fields = global_readonly_fields
    
class PBSMMLightSeasonAdmin(admin.ModelAdmin):
    readonly_fields = global_readonly_fields
    
class PBSMMLightShowAdmin(admin.ModelAdmin):
    readonly_fields = global_readonly_fields
    
class PBSMMLightSpecialAdmin(admin.ModelAdmin):
    readonly_fields = global_readonly_fields
    
    
admin.site.register(PBSMMLightAsset, PBSMMLightAssetAdmin)
#admin.site.register(PBSMMLightCollection, PBSMMLightAssetAdmin)
admin.site.register(PBSMMLightEpisode, PBSMMLightAssetAdmin)
#admin.site.register(PBSMMLightFranchise, PBSMMLightAssetAdmin)
#admin.site.register(PBSMMLightRemoteAsset, PBSMMLightAssetAdmin)
admin.site.register(PBSMMLightSeason, PBSMMLightAssetAdmin)
admin.site.register(PBSMMLightShow, PBSMMLightAssetAdmin)
admin.site.register(PBSMMLightSpecial, PBSMMLightAssetAdmin)