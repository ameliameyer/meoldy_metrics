# imports
import streamlit as st # import streamlit app
import pandas as pd

from spotify_api import (
    authenticate_spotify
  , get_user_top_tracks
  , get_playlist_tracks
)
from utils import (
    extract_audio_features
  , clean_track_data
)

# create the page title
st.set_page_config(
    page_title='Spotify Track Analyzer'
  , layout='wide'
)

st.title('Spotify Track Analyzer')

# create side bar
with st.sidebar:
  st.header('Connect Your Spotify')
  auth_code = st.text_input('Enter your Spotify auth code:')
  data_source = st.radio('Choose data source:', ['Top Tracks', 'Playlist'])
  time_range = st.selectbox('Time Range (for Top Tracks)', ['short_term', 'medium_term', 'long_term'])
  playlist_id = st.text_input('Playlist ID (if Playlist selected)')
  fetch_button = st.button('Fetch Data')

if fetch_button and auth_code:
  sp = authenticate_spotify(auth_code)

  if not sp:
    st.error('Authentication failed. Check your auth code.')
  else:
    with st.spinner('Fetching tracks...'):
      if data_source == 'Top Tracks':
        tracks = get_user_top_tracks(sp, time_range=time_range)
      else:
        tracks = get_playlist_tracks(sp, playlist_id)

      if not tracks:
        st.warning('No tracks found.')
      else:
        with st.spinner('Getting audio features...'):
          audio_features = extract_audio_features(sp, tracks)
          df = clean_track_data(tracks, audio_features)

        st.success(f'Found {len(df)} tracks')
        st.dataframe(df)

        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label='Download CSV'
          , data=csv
          , file_name='spotify_tracks.csv'
          , mime='text/csv'
        )
