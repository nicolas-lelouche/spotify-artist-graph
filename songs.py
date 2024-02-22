import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())


artists = []
with open('artist-list.txt') as my_file:
    for line in my_file:
        artists.append(line.strip())

dict_uri = dict()

for artist in artists:    
    results = spotify.search(q='artist:' + artist, type='artist', limit=1)
    items = results['artists']['items']
    if len(items) == 1:
        name = items[0]['name']
        uri = items[0]['uri']
        dict_uri[name] = uri
    else:
        print('Error')

dict_album = dict()

for key in dict_uri:
    albums = spotify.artist_albums(dict_uri[key], album_type='album')['items']
    album_list = []
    for album in albums:
        album_list.append(album['id'])
    dict_album[key] = album_list

dict_songs = dict()

for key in dict_album:
    albums_info = spotify.albums(dict_album[key])['albums']
    for album in albums_info:
        tracks = album['tracks']['items']
        for track in tracks:
            artists = track['artists']
            song_artists = []
            for artist in artists:
                song_artists.append(artist['name'])
            dict_songs[track['name']] = song_artists
            #TODO: Add vertex to our graph here.

print(dict_songs)


'''
for key in dict_album:
    print(key)
    for album in dict_album[key]:
        tracks = spotify.album_tracks(album)
        print(len(tracks['items']))
'''
