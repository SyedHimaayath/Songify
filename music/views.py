from django.http import Http404, HttpResponse
from django.shortcuts import render
from .models import Album, Song

def index(request):
    details = Album.objects.all()
    c = {"details":details}
    return render(request, 'home.html', c)

def detail(request, album_id):
    try:
        album = Album.objects.get(pk=album_id)
    except Album.DoesNotExist:
        raise Http404("Album does not exist")
    if album:
        song = Song.objects.filter(album=album_id)
    return render(request, 'detail.html', {'song':song})

def songs(request):
    try:
        song = Song.objects.all()
    except Song.DoesNotExist:
        raise Http404("Can't find songs")
    return render(request, 'songs.html', {'song':song})