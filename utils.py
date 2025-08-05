import pandas as pd

def flatten_track_data(track, features):
    """
    Combines basic track data with audio features into a single flat dictionary.
    """
    return {
        , 'track_name': track['name']
        , 'track_id': track['id']
        , 'artist_name': track['artists'][0]['name']
        , 'artist_id': track['artists'][0]['id']
        , 'album_name': track['album']['name']
        , 'album_id': track['album']['id']
        , 'release_date': track['album']['release_date']
        , 'popularity': track['popularity']
        , 'duration_ms': track['duration_ms']
        , 'explicit': track['explicit']
        , 'danceability': features.get('danceability')
        , 'energy': features.get('energy')
        , 'key': features.get('key')
        , 'loudness': features.get('loudness')
        , 'mode': features.get('mode')
        , 'speechiness': features.get('speechiness')
        , 'acousticness': features.get('acousticness')
        , 'instrumentalness': features.get('instrumentalness')
        , 'liveness': features.get('liveness')
        , 'valence': features.get('valence')
        , 'tempo': features.get('tempo')
        , 'time_signature': features.get('time_signature')
    }

def tracks_to_dataframe(tracks_with_features):
    """
    Converts a list of flattened track dictionaries into a pandas DataFrame.
    """
    return pd.DataFrame(tracks_with_features)

def get_valid_track_ids(tracks):
    """
    Returns a list of valid Spotify track IDs from a list of track dicts.
    """
    return [track['id'] for track in tracks if track.get('id')]


