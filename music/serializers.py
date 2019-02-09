<<<<<<< HEAD
from rest_framework import serializers
from . models import Album, Song, UserSongs, Recommendation


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ('song_name', 'album_name', 'song_file')


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ('album_name', 'artist_name', 'album_cover', 'genre')


class UserSongSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSongs
        fields = ('song', 'user')


class RecommendationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recommendation
        fields = ('recommended_by', 'recommended_to', 'recommended_song')
=======
from rest_framework import serializers
from . models import Album, Song, UserSongs, Recommendation


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ('song_name', 'album_name', 'song_file')


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ('album_name', 'artist_name', 'album_cover', 'genre')


class UserSongSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSongs
        fields = ('song', 'user')


class RecommendationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recommendation
        fields = ('recommended_by', 'recommended_to', 'recommended_song')
>>>>>>> 1dec1ff361299080e76c8789214accf677b3fef6
