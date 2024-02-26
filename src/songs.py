import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

def get_artist_list(filepath):
    artists = []
    with open(filepath) as my_file:
        for line in my_file:
            artists.append(line.strip())
    
    return artists

def get_artists_uri(artists):
    
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

    return dict_uri

def get_artist_albums(artists_uri):
    
    dict_album = dict()

    for key in artists_uri:
        albums = spotify.artist_albums(artists_uri[key], album_type='album')['items']
        album_list = []
        for album in albums:
            album_list.append(album['id'])
        dict_album[key] = album_list

    return dict_album

def get_songs(filepath):

    dict_songs = dict()
    number_of_artist_appearance = dict()

    artists = get_artist_list(filepath)
    artists_uri = get_artists_uri(artists)
    albums = get_artist_albums(artists_uri)
    
    for key in albums:
        albums_info = spotify.albums(albums[key])['albums']
        for album in albums_info:
            tracks = album['tracks']['items']
            for track in tracks:
                artists = track['artists']
                song_artists = []
                for artist in artists:
                    song_artists.append(artist['name'])
                    if artist['name'] in number_of_artist_appearance:
                        number_of_artist_appearance[artist['name']] += 1
                    else:
                        number_of_artist_appearance[artist['name']] = 1
                dict_songs[track['name']] = song_artists
    
    return dict_songs, number_of_artist_appearance
