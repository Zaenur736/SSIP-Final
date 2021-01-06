from django.shortcuts import render
from catalog.models.album import Album
from django.contrib.auth.decorators import login_required
from catalog.forms import AlbumForm
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

@login_required
def listalbum(request):
    listalbums = Album.objects.order_by('-year')
    data = {
        'listalbums': listalbums,
    }
    return render(request, 'album/album.html', context=data)

def add_album(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST)  # we accept post request from submit button
        if form.is_valid():  # django has its own validation
            form.save()  # directly save the form
            return HttpResponseRedirect(reverse('listalbum'))  # return to all authors page
    else:
        form = AlbumForm()  # pass empty form

    context = {
        'form': form
    }
    return render(request, 'album/add_album.html', context=context)
