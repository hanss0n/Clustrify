from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import pandas as pd
import numpy as np


def __track_to_arr(feature_dict, features):
    song_id = feature_dict[0]
    track = [song_id]
    for i in range(len(features)):
        track.append(feature_dict[1][features[i]])
    return track


def __to_data_frame(song_list, cluster_features):
    tracks = []
    for song in song_list.items():
        tracks.append(__track_to_arr(song, cluster_features))

    song_data = pd.DataFrame(tracks, columns=['id'] + cluster_features)
    df_labels = song_data['id']
    df_songs = song_data[cluster_features]

    return df_songs, df_labels


def __cluster_data_frame(df_songs, df_labels, num_cluster):
    df_songs = np.array(df_songs)
    std_scaler = StandardScaler()
    std_scaler.fit(df_songs)
    df_songs_scaled = std_scaler.transform(df_songs)

    kmeans = KMeans(n_clusters=num_cluster, init='k-means++', random_state=111)
    kmeans_labels = kmeans.fit(df_songs_scaled).labels_

    cluster_dict = {}
    for song_id, cluster_label in enumerate(kmeans_labels):
        cluster_dict[df_labels[song_id]] = cluster_label

    return cluster_dict


def cluster(song_list, features, num_clusters):
    df_songs, df_labels = __to_data_frame(song_list, features)
    return __cluster_data_frame(df_songs, df_labels, num_clusters)
