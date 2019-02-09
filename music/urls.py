<<<<<<< HEAD
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('albums', views.AlbumView)
router.register('songs', views.SongView)
router.register('user-songs', views.SongUserView)
router.register('recommendation', views.RecommendationView)

urlpatterns = [
    path('api/', include(router.urls)),
    path('', views.AlbumList.as_view(), name='album-list'),
    path('detail/<int:pk>', views.AlbumDetail.as_view(), name='album-detail'),
    path('create', views.AlbumCreate.as_view(), name='album-create'),
    path('update/<int:pk>', views.AlbumUpdate.as_view(), name='album-update'),
    path('delete/<int:pk>', views.AlbumDelete.as_view(), name='album-delete'),
    path('about/<int:pk>', views.AlbumSong.as_view(), name='album-song'),

    # Path for songs start here
    path('song/list', views.SongList.as_view(), name='song-list'),
    path('song/detail/<int:pk>', views.SongDetail.as_view(), name='song-detail'),
    path('song/create', views.SongCreate.as_view(), name='song-create'),
    path('song/update/<int:pk>', views.SongUpdate.as_view(), name='song-update'),
    path('song/delete/<int:pk>', views.SongDelete.as_view(), name='song-delete'),
    path('song/add_song', views.add_song, name='add-song'),
]

=======
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('albums', views.AlbumView)
router.register('songs', views.SongView)
router.register('user-songs', views.SongUserView)
router.register('recommendation', views.RecommendationView)

urlpatterns = [
    path('api/', include(router.urls)),
    path('', views.AlbumList.as_view(), name='album-list'),
    path('detail/<int:pk>', views.AlbumDetail.as_view(), name='album-detail'),
    path('create', views.AlbumCreate.as_view(), name='album-create'),
    path('update/<int:pk>', views.AlbumUpdate.as_view(), name='album-update'),
    path('delete/<int:pk>', views.AlbumDelete.as_view(), name='album-delete'),
    path('about/<int:pk>', views.AlbumSong.as_view(), name='album-song'),

    # Path for songs start here
    path('song/list', views.SongList.as_view(), name='song-list'),
    path('song/detail/<int:pk>', views.SongDetail.as_view(), name='song-detail'),
    path('song/create', views.SongCreate.as_view(), name='song-create'),
    path('song/update/<int:pk>', views.SongUpdate.as_view(), name='song-update'),
    path('song/delete/<int:pk>', views.SongDelete.as_view(), name='song-delete'),
    path('song/add_song', views.add_song, name='add-song'),
]

>>>>>>> 1dec1ff361299080e76c8789214accf677b3fef6
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)