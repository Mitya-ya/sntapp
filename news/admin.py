from django.contrib import admin
from .models import Post, Indications, Area, IndicationsDate, Subscriber

admin.site.register(Post)
admin.site.register(Indications)
admin.site.register(Area)
admin.site.register(IndicationsDate)
admin.site.register(Subscriber)
