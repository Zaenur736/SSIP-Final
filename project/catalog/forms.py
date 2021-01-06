from django.forms import ModelForm
from django.core.exceptions import ValidationError
from catalog.models.singer import Singer
from catalog.models.song import Song
from catalog.models.album import Album

class SongForm(ModelForm):
    class Meta:
        model = Song  # model to use in form
        # list of fields to be displayed
        fields = ['title', 'genre', 'album', 'songwriter', 'singer']

class SingerForm(ModelForm):
    class Meta:
        model = Singer  # model to use in form
        # list of fields to be displayed
        fields = ['first_name','last_name','date_of_birth']

class AlbumForm(ModelForm):
    class Meta:
        model = Album  # model to use in form
        # list of fields to be displayed
        fields = ['name','year','singer']