import os
from django.core.exceptions import ValidationError


def validate_song_extension(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.wav', '.mp3', '.aac']
    if not ext.lower() in valid_extensions:
        raise ValidationError(u'Unsupported file extension for the Song.')


def validate_cover_extension(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.jpg', '.png']
    if not ext.lower() in valid_extensions:
        raise ValidationError(u'Unsupported file extension for the Album Cover.')