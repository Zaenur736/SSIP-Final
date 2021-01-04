from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('songs/', views.list_songs, name='songs'),
    path('song/add', views.add_song, name='add_song'),
    path('song/edit/<int:song_id>', views.edit_song, name='edit_song'),
    path('song/delete/<int:song_id>', views.delete_song, name='delete_song'),
    path('songwriters/', views.list_songwriters, name='songwriters'),
    path('songwriter/add', views.add_songwriter, name='add_songwriter'),
    path('songwriter/edit/<int:songwriter_id>', views.edit_songwriter, name='edit_songwriter'),
    path('songwriter/delete/<int:songwriter_id>', views.delete_songwriter, name='delete_songwriter'),
    path('releases/', views.list_releases, name='releases'),
]
