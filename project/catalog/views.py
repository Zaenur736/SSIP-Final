from django.forms.models import model_to_dict
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from catalog.models import Song, SongWriter, Release
from catalog.forms import SongWriterForm, SongForm


def index(request):
    # get all info here including authors, songs, and genres
    num_songs = Song.objects.all().count()
    num_songwriters = SongWriter.objects.all().count()
    num_releases = Release.objects.all().count()
    context = {
        'num_songs': num_songs,
        'num_songwriters': num_songwriters,
        'num_releases': num_releases,
    }
    return render(request, 'index.html', context=context)


def list_songwriters(request):
    songwriters = SongWriter.objects.all()
    context = {
        'songwriters': songwriters,
    }
    return render(request, 'songwriters.html', context=context)


def list_songs(request):
    songs = Song.objects.all()
    context = {
        'songs': songs,
    }
    return render(request, 'songs.html', context=context)


def list_releases(request):
    releases = Release.objects.all()
    context = {
        'releases': releases,
    }
    return render(request, 'releases.html', context=context)


def add_songwriter(request):
    if request.method == 'POST':
        form = SongWriterForm(request.POST)
        if form.is_valid():
            form.save()  # directly save the form
            return HttpResponseRedirect(reverse('songwriters'))
    else:
        form = SongWriterForm()

    context = {
        'form': form
    }
    return render(request, 'songwriter_form.html', context=context)


def edit_songwriter(request, songwriter_id):
    if request.method == 'POST':
        songwriter = SongWriter.objects.get(pk=songwriter_id)
        form = SongWriterForm(request.POST, instance=songwriter)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('songwriters'))
    else:
        songwriter = SongWriter.objects.get(pk=songwriter_id)
        fields = model_to_dict(songwriter)
        form = SongWriterForm(initial=fields, instance=songwriter)
    context = {
        'form': form,
        'type': 'edit',
    }
    return render(request, 'songwriter_form.html', context=context)


def delete_songwriter(request, songwriter_id):
    songwriter = SongWriter.objects.get(pk=songwriter_id)
    if request.method == 'POST':
        songwriter.delete()
        return HttpResponseRedirect(reverse('songwriters'))
    context = {
        'songwriter': songwriter
    }
    return render(request, 'songwriter_delete_form.html', context=context)


def add_song(request):
    if request.method == 'POST':
        form = SongForm(request.POST)
        if form.is_valid():
            form.save()  # directly save the form
            return HttpResponseRedirect(reverse('songs'))
    else:
        form = SongForm()

    context = {
        'form': form
    }
    return render(request, 'song_form.html', context=context)


def edit_song(request, song_id):
    if request.method == 'POST':
        song = Song.objects.get(pk=song_id)
        form = SongForm(request.POST, instance=song)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('songs'))
    else:
        song = Song.objects.get(pk=song_id)
        fields = model_to_dict(song)
        form = SongForm(initial=fields, instance=song)
    context = {
        'form': form,
        'type': 'edit',
    }
    return render(request, 'song_form.html', context=context)


def delete_song(request, song_id):
    song = Song.objects.get(pk=song_id)
    if request.method == 'POST':
        song.delete()
        return HttpResponseRedirect(reverse('songs'))
    context = {
        'song': song,
    }
    return render(request, 'song_delete_form.html', context=context)
