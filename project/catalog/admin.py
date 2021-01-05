from django.contrib import admin
from catalog.models import song, songwriter, singer, album, genre, release

admin.site.register(song.Song)
admin.site.register(singer.Singer)
admin.site.register(release.Release)
admin.site.register(album.Album)
admin.site.register(songwriter.SongWriter)
admin.site.register(genre.Genre)

