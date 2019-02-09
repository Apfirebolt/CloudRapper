<<<<<<< HEAD
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse, reverse_lazy
from . validators import validate_cover_extension, validate_song_extension


class Album(models.Model):
    album_name = models.CharField(max_length=100)
    artist_name = models.CharField(max_length=100)
    genre = models.CharField(max_length=30)
    album_cover = models.ImageField(upload_to='album_covers/', null=True,
                                   validators=[validate_cover_extension])

    def get_absolute_url(self):
        return reverse('music:album-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.album_name


class Song(models.Model):
    song_name = models.CharField(max_length=100)
    album_name = models.ForeignKey(Album, on_delete=models.CASCADE)
    song_file = models.FileField(upload_to='songs/', null=True,
                                 validators=[validate_song_extension])

    def get_absolute_url(self):
        return reverse('music:song-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.song_name


class Recommendation(models.Model):
    recommended_by = models.ForeignKey(User, related_name='user_by', on_delete=models.CASCADE)
    recommended_to = models.ForeignKey(User, related_name='user_to', on_delete=models.CASCADE)
    recommended_song = models.ForeignKey(Song, on_delete=models.CASCADE)

    def __str__(self):
        return self.recommended_song.song_name


class UserSongs(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)

    def __str__(self):
        return self.song.song_name + " - " + self.user.username
=======
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse, reverse_lazy
from . validators import validate_cover_extension, validate_song_extension


class Album(models.Model):
    album_name = models.CharField(max_length=100)
    artist_name = models.CharField(max_length=100)
    genre = models.CharField(max_length=30)
    album_cover = models.ImageField(upload_to='album_covers/', null=True,
                                   validators=[validate_cover_extension])

    def get_absolute_url(self):
        return reverse('music:album-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.album_name


class Song(models.Model):
    song_name = models.CharField(max_length=100)
    album_name = models.ForeignKey(Album, on_delete=models.CASCADE)
    song_file = models.FileField(upload_to='songs/', null=True,
                                 validators=[validate_song_extension])

    def get_absolute_url(self):
        return reverse('music:song-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.song_name


class Recommendation(models.Model):
    recommended_by = models.ForeignKey(User, related_name='user_by', on_delete=models.CASCADE)
    recommended_to = models.ForeignKey(User, related_name='user_to', on_delete=models.CASCADE)
    recommended_song = models.ForeignKey(Song, on_delete=models.CASCADE)

    def __str__(self):
        return self.recommended_song.song_name


class UserSongs(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)

    def __str__(self):
        return self.song.song_name + " - " + self.user.username
>>>>>>> 1dec1ff361299080e76c8789214accf677b3fef6
