from django.db import models
from catalog.models.genre import Genre
from catalog.models.album import Album
from catalog.models.songwriter import SongWriter
from catalog.models.singer import Singer

class Song(models.Model) :
    """ song data """ 
    title = models.CharField(max_length=200)
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL,null=True)
    album = models.ForeignKey(Album, on_delete=models.SET_NULL,null=True)
    songwriter = models.ManyToManyField(SongWriter)
    singer = models.ForeignKey(Singer, on_delete=models.SET_NULL,null=True)
    
    class Meta:
        app_label = 'catalog'

    def __str__ (self):
        return f'{self.title}'