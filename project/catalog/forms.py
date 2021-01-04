from django.forms import ModelForm
from django.core.exceptions import ValidationError
from catalog.models import Song, SongWriter


class SongWriterForm(ModelForm):
    class Meta:
        model = SongWriter  # model to use in form
        # list of fields to be displayed
        fields = ['first_name', 'last_name', 'date_of_birth']


class SongForm(ModelForm):
    class Meta:
        model = Song  # model to use in form
        # list of fields to be displayed
        fields = ['title', 'songwriter', 'release', 'genre']
