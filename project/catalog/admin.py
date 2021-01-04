from django.contrib import admin
from .models import Song, SongWriter, Release


admin.site.register(Song)
admin.site.register(SongWriter)
admin.site.register(Release)
