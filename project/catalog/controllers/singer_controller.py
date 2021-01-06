from django.shortcuts import render
from catalog.models.singer import Singer
from django.contrib.auth.decorators import login_required
from catalog.forms import SingerForm
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

@login_required
def listsinger(request):
    listsingers = Singer.objects.all()
    data = {
        'listsingers': listsingers,
    }
    return render(request, 'singer/singer.html', context=data)

def add_singer(request):
    if request.method == 'POST':
        form = SingerForm(request.POST)  # we accept post request from submit button
        if form.is_valid():  # django has its own validation
            form.save()  # directly save the form
            return HttpResponseRedirect(reverse('listsinger'))  # return to all authors page
    else:
        form = SongForm()  # pass empty form

    context = {
        'form': form
    }
    return render(request, 'singer/add_singer.html', context=context)
