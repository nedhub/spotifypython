import spotipy
from spotipy.client import Spotify


from spotipy.oauth2 import SpotifyOAuth
import json



scope = "playlist-modify-public"
username= "31yg6qur7sttckpcwg2lsrjp5h4u"


token = SpotifyOAuth(scope=scope, username=username)

spotifyObject = spotipy.Spotify(auth_manager= token)

#create the playlist


playlist_name = input("Enter a playlist name:")
playlist_description = input("Enter a playlist description:")


spotifyObject.user_playlist_create(user=username, name=playlist_name, public=True, description=playlist_description)

