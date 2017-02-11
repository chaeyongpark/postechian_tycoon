from django.contrib import admin
from .models import Map, Close, Item, Avatar, Combination, Title, Contain, CodeToItem, CombinationContain, Mission 

admin.site.register(Avatar)
admin.site.register(Item)
admin.site.register(Combination)
admin.site.register(Title)
admin.site.register(Contain)
admin.site.register(CodeToItem)
admin.site.register(CombinationContain)
admin.site.register(Mission)
admin.site.register(Close)
admin.site.register(Map)