from django.shortcuts import render, redirect
from app.models import Album, Song
from django.views import View


class AlbumList(View):
    def get(self, request):
        title = Album.objects.all()
        return render(request, "album_list.html", {"albums": title})


class NewSong(View):
    def post(self, request, id):
        album = Album.objects.get(id=id)
        Song.objects.create(
            title=request.POST["title"], album=album, seconds=request.POST["seconds"]
        )
        return redirect("album_detail", id)


class AlbumDetail(View):
    def get(self, request, id):
        album = Album.objects.get(id=id)
        return render(request, "album_detail.html", {"album": album})
