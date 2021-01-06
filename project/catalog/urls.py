from django.urls import path
from catalog.controllers import song_controller, album_controller, singer_controller, registration_controller


urlpatterns = [ 
    path('',song_controller.index, name='index'),
    path('song/',song_controller.listsong, name='listsong'),
    path('album/',album_controller.listalbum, name='listalbum'),
    path('singer/',singer_controller.listsinger, name='listsinger'),
    path('register/', registration_controller.index, name='register'),
    path('song/add', song_controller.add_song, name='add_song'),
    path('song/delete/<int:song_id>', song_controller.delete_song, name='delete_song'),
    path('singer/add', singer_controller.add_singer, name='add_singer'),
    path('album/add', album_controller.add_album, name='add_album'),

]