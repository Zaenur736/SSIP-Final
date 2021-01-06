from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from catalog.models.song import Song
from catalog.forms import SongForm
from django.forms.models import model_to_dict
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


@login_required
def index(request):
    songs = Song.objects.all()
    data = {
        'songs': songs,
    }
    return render(request, 'catalog/index.html', context=data)
    
@login_required
def listsong(request):
    listsongs = Song.objects.all()
    data = {
        'listsongs': listsongs,
    }
    return render(request, 'song/song.html', context=data)

def add_song(request):
    if request.method == 'POST':
        form = SongForm(request.POST)  # we accept post request from submit button
        if form.is_valid():  # django has its own validation
            form.save()  # directly save the form
            return HttpResponseRedirect(reverse('listsong'))  # return to all authors page
    else:
        form = SongForm()  # pass empty form

    context = {
        'form': form
    }
    return render(request, 'song/add_song.html', context=context)

def delete_song(request, song_id):
    song = Song.objects.get(pk=song_id)
    if request.method == 'POST':
        song.delete()
        return HttpResponseRedirect(reverse('listsong'))
    context = {
        'song': song
    }
    return render(request, 'song/delete_song.html', context=context)
