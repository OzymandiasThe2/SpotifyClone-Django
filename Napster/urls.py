from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views
from django.urls import include, re_path
# from .views import UserRegiForm

app_name = "Napster"

urlpatterns = [
    # path("", views.index, name="index"),
    # path("add/", views.submit_music, name="submit_music"),
    # path("register/", UserRegiForm.as_view(), name="register"),
    # path("view/", views.view, name="view"),
    # path(r'^songs/(?P<filter_by>[a-zA_Z]+)/$', views.songs, name='songs'),
    path("profile/", views.profile, name="profile"),
    re_path(r'^$', views.index, name='index'),
    re_path(r'^register/$', views.register, name='register'),
    re_path(r'^login_user/$', views.login_user, name='login_user'),
    re_path(r'^logout_user/$', views.logout_user, name='logout_user'),
    re_path(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),
    re_path(r'^(?P<song_id>[0-9]+)/favorite/$', views.favorite, name='favorite'),
    re_path(r'^songs/(?P<filter_by>[a-zA_Z]+)/$', views.songs, name='songs'),
    re_path(r'^create_album/$', views.create_album, name='create_album'),
    re_path(r'^(?P<album_id>[0-9]+)/create_song/$', views.create_song, name='create_song'),
    re_path(r'^(?P<album_id>[0-9]+)/delete_song/(?P<song_id>[0-9]+)/$', views.delete_song, name='delete_song'),
    re_path(r'^(?P<album_id>[0-9]+)/favorite_album/$', views.favorite_album, name='favorite_album'),
    re_path(r'^(?P<album_id>[0-9]+)/delete_album/$', views.delete_album, name='delete_album'),
]