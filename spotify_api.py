# imports
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# create function to authenticate spotify 
def authenticate_spotify(client_id, client_secret, redirect_uri, scope=None):
    if scope is None:
        scope = "user-top-read playlist-read-private"

    auth_manager = SpotifyOAuth(
        client_id=client_id,
        client_secret=client_secret,
        redirect_uri=redirect_uri,
        scope=scope
    )
    return spotipy.Spotify(auth_manager=auth_manager)

# get the top 100 tracks from the user's library
def get_top_tracks_with_features(sp, total=100, time_range='long_term'):
    top_tracks = []
    for offset in range(0, total, 50):
        results = sp.current_user_top_tracks(limit=50, offset=offset, time_range=time_range)
        top_tracks.extend(results['items'])

    track_ids = [track['id'] for track in top_tracks if track['id']]
    features_list = sp.audio_features(track_ids)

# get the track features
    enriched_tracks = []
    for track, features in zip(top_tracks, features_list):
        enriched = {
            'track_name': track['name']
            , 'artist_name': track['artists'][0]['name']
            , 'album_name': track['album']['name']
            , 'release_date': track['album']['release_date']
            , 'popularity': track['popularity']
            , 'duration_ms': track['duration_ms']
            , 'explicit': track['explicit']
            , 'track_number': track['track_number']
            , 'disc_number': track['disc_number']
            , 'danceability': features['danceability']
            , 'energy': features['energy']
            , 'key': features['key']
            , 'loudness': features['loudness']
            , 'mode': features['mode']
            , 'speechiness': features['speechiness']
            , 'acousticness': features['acousticness']
            , 'instrumentalness': features['instrumentalness']
            , 'liveness': features['liveness']
            , 'valence': features['valence']
            , 'tempo': features['tempo']
            , 'time_signature': features['time_signature']
        }
        enriched_tracks.append(enriched)

    return enriched_tracks

# function to get the user's playlist
def get_playlist_tracks_with_features(sp, playlist_id):
    results = sp.playlist_tracks(playlist_id)
    playlist_tracks = results['items']

    while results['next']:
        results = sp.next(results)
        playlist_tracks.extend(results['items'])

    track_items = [item['track'] for item in playlist_tracks if item['track']]
    track_ids = [track['id'] for track in track_items if track['id']]
    features_list = sp.audio_features(track_ids)

    enriched_tracks = []
    for track, features in zip(track_items, features_list):
        enriched = {
            'track_name': track['name']
            , 'artist_name': track['artists'][0]['name']
            , 'album_name': track['album']['name']
            , 'release_date': track['album']['release_date']
            , 'popularity': track['popularity']
            , 'duration_ms': track['duration_ms']
            , 'explicit': track['explicit']
            , 'track_number': track['track_number']
            , 'disc_number': track['disc_number']
            , 'danceability': features['danceability']
            , 'energy': features['energy']
            , 'key': features['key']
            , 'loudness': features['loudness']
            , 'mode': features['mode']
            , 'speechiness': features['speechiness']
            , 'acousticness': features['acousticness']
            , 'instrumentalness': features['instrumentalness']
            , 'liveness': features['liveness']
            , 'valence': features['valence']
            , 'tempo': features['tempo']
            , 'time_signature': features['time_signature']
        }
        enriched_tracks.append(enriched)

    return enriched_tracks

