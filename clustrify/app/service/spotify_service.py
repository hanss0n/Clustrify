import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os
import numbers

# Set environment variables 'SPOTIPY_CLIENT_ID' and 'SPOTIPY_CLIENT_SECRET'
client_id = os.environ.get('SPOTIPY_CLIENT_ID')
client_secret = os.environ.get('SPOTIPY_CLIENT_SECRET')
client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


def get_tracks_by_list_id(playlist_uri):
    playlist = spotify.playlist_tracks(playlist_uri, fields='items.track.id, items.track.name, '
                                                            'items.track.preview_url, '
                                                            'items.track.artists.name,'
                                                            'items.track.external_urls.spotify,'
                                                            'items.track.album.images')['items']

    return list(filter(lambda x: x["track"]["id"] is not None, playlist))


def fetch_features(track_ids, features_to_consider):
    # Fetch the audio features of each track
    features = spotify.audio_features(track_ids)

    # Check that there are any elements fetched, otherwise raise an exception
    if any(features):
        # Store by id for simplicity
        features_by_track_id = {features[i]['id']: features[i] for i in range(len(features))}

        # Filter out unwanted features
        filtered_features_by_id = filter_features(features_by_track_id, features_to_consider)

        # Rescale the Key, Loudness and Tempo features to [0, 1], if they are considered
        scaled_features = rescale_features(filtered_features_by_id)

        return scaled_features
    else:
        raise spotipy.SpotifyException(404, -1, 'Invalid Track Id')


def filter_features(features_by_id, features_to_consider):
    if not bool(features_to_consider):
        features_to_consider = ['acousticness', 'danceability', 'energy', 'instrumentalness', 'speechiness']

    for track_features in features_by_id.items():
        # Filter out the unwanted features
        # If features_to_consider is empty, all numerical features will be used (except time_signature and duration)
        filtered_features = {feature: value for (feature, value) in track_features[1].items() if
                             isinstance(value, numbers.Number) and feature in features_to_consider}

        # Neither duration_ms nor time_signature will be considered
        if 'time_signature' in filtered_features:
            del filtered_features['time_signature']
        if 'duration_ms' in filtered_features:
            del filtered_features['duration_ms']

        # Replace the non-filtered features
        features_by_id[track_features[0]] = filtered_features

    return features_by_id


def rescale_features(features):
    for track_features in features.items():

        rescaled_features = track_features[1]

        # Rescale the Key, Loudness, Tempo and time_signature features to [0, 1]
        # Key is denoted by standard Pitch Class notation, where -1 is used if no key is detected
        # We alter the current notation, [-1, 11] --> [0, 1]
        if 'key' in rescaled_features.keys():
            rescaled_features['key'] += 1
            rescaled_features['key'] /= 12

        # Loudness is previously measured in decibel, in range [-60, 0]. We want [0, 1]
        if 'loudness' in rescaled_features.keys():
            rescaled_features['loudness'] += 60
            rescaled_features['loudness'] /= 60

        # Tempo is measured in BPM. Spotify seems to measure up to 250 BPM, which is why this values is used for scaling
        if 'tempo' in rescaled_features.keys():
            rescaled_features['tempo'] /= 250

        # Save the update values
        features[track_features[0]] = rescaled_features

    return features


def fetch_track(track_id):
    return spotify.track(track_id)
