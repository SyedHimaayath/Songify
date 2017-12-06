from django.http import Http404, HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Album, Song

def index(request):
    details = Album.objects.all()
    c = {"details":details}
    return render(request, 'home.html', c)

def detail(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    return render(request, 'detail.html', {'album':album})

def songs(request):
    try:
        song = Song.objects.all()
    except Song.DoesNotExist:
        raise Http404("Can't find songs")
    return render(request, 'songs.html', {'song':song})