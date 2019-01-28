from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='dashboard'),
    path('general_settings/<int:pk>', views.GeneralSettings.as_view(), name='profile_settings'),
    path('settings/<int:pk>', views.ChangeSettings.as_view(), name='settings'),
    path('user_login/', views.user_login, name='user_login'),
    path('register/',views.register, name='register'),
    path('user_logout/',views.user_logout, name='user_logout'),
    path('people/',views.all_users, name='all_users'),
    path('saved_songs/',views.saved_songs, name='saved_songs'),
    path('recommend_song/<int:pk>',views.recommend_song, name='recommend_song'),
    path('recommend_ajax',views.recommend_ajax, name='recommend_ajax'),
    path('add_friend',views.add_friend, name='add_friend'),

    # Test page url
    path('test/',views.test, name='test'),
]
