from django.contrib import admin
from .models import Item, Avatar, Combination, Title, Contain, CodeToItem, CombinationContain 

admin.site.register(Avatar)
admin.site.register(Item)
admin.site.register(Combination)
admin.site.register(Title)
admin.site.register(Contain)
admin.site.register(CodeToItem)
admin.site.register(CombinationContain)
