from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView, View
from . models import Album, Song, UserSongs, Recommendation
from django.urls import reverse_lazy
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from . serializers import SongSerializer, AlbumSerializer, UserSongSerializer, RecommendationSerializer
import os


def index_view(request):
    return render(request, 'music/music_home.html')


class AlbumList(ListView):
    template_name = 'music/album_list.html'
    queryset = Album.objects.all()


class AlbumDetail(DetailView):
    model = Album

    template_name = 'music/album_detail.html'
    queryset = Album.objects.all()


class AlbumCreate(CreateView):
    model = Album
    fields = ['album_name', 'artist_name', 'genre', 'album_cover']


class AlbumUpdate(UpdateView):
    model = Album
    fields = ['album_name', 'artist_name', 'genre', 'album_cover']


class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('music:album-list')


class AlbumSong(View):

    def get(self, request, *args, **kwargs):
        album = Album.objects.filter(pk=self.kwargs['pk'])
        return render(request, 'music/album_about.html', {'album' : album})


# CRUD for songs begins here
class SongList(ListView):
    template_name = 'music/song_list.html'
    queryset = Song.objects.all()


class SongDetail(DetailView):
    model = Song

    template_name = 'music/song_detail.html'
    queryset = Song.objects.all()


class SongCreate(CreateView):
    model = Song
    fields = ['album_name', 'song_name', 'song_file']


class SongUpdate(UpdateView):
    model = Song
    fields = ['album_name', 'song_name', 'song_file']


class SongDelete(DeleteView):
    model = Song
    success_url = reverse_lazy('music:song-list')


class AlbumView(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        return Response("ok")


class SongView(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

    def post(self, request, format=None):
        return Response("ok")


class SongUserView(viewsets.ModelViewSet):
    queryset = UserSongs.objects.all()
    serializer_class = UserSongSerializer

    def post(self, request, format=None):
        return Response("ok")


class RecommendationView(viewsets.ModelViewSet):
    queryset = Recommendation.objects.all()
    serializer_class = RecommendationSerializer

    def post(self, request, format=None):
        return Response("ok")


# Function Based Views to handle API Ajax requests
def add_song(request):
    if request.method == 'POST':
        song_name = request.POST.get('song_name')
        user_name = request.POST.get('user_name')

        print(song_name)
        print(user_name)

        user_instance = User.objects.get(username=user_name)
        song_instance = Song.objects.get(song_name=song_name)

        user_song = UserSongs.objects.create(user=user_instance, song=song_instance)
        user_song.save()

    return HttpResponse(status=204)