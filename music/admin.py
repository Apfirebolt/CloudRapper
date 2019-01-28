from django.contrib import admin
from . models import Song, Album, Recommendation, UserSongs


class AlbumAdmin(admin.ModelAdmin):
    fields = ['artist_name', 'album_name', 'genre', 'album_cover']

    search_fields = ['artist_name']

    list_filter = ['genre']


class SongAdmin(admin.ModelAdmin):
    fields = ['song_name', 'album_name', 'song_file']

    search_fields = ['song_name']

    list_filter = ['album_name']


class RecommendationAdmin(admin.ModelAdmin):
    fields = ['recommended_to', 'recommended_by', 'recommended_song']


admin.site.register(Song, SongAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Recommendation, RecommendationAdmin)
admin.site.register(UserSongs)
