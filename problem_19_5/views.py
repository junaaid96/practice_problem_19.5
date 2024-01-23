from django.shortcuts import render
from album.models import Album
from musician.models import Musician


def home(request):
    albums = Album.objects.all()
    musicians = Musician.objects.all()
    zipped = zip(albums, musicians)
    return render(request, 'home.html', {'zipped_data': zipped})