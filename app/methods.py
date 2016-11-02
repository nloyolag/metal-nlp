import pandas as pd
import numpy as np
import sklearn
import joblib
import re
import os
import csv
from sklearn.externals import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from app import APP_STATIC, APP_ROOT

def predict_cluster(artist):

    # Get dataframes containing cluster information
    data = pd.read_pickle(os.path.join(APP_STATIC, 'data/clustered_lyrics.pkl'))
    original_data = pd.read_pickle(os.path.join(APP_STATIC, 'data/data_filtered_original.pkl'))
    initial_artist = artist
    artist = initial_artist.lower()

    # Check if artist appears in data
    artist_row = data[data.artist == artist]
    if len(artist_row) != 1:
        return None

    # Get cluster and properties for given artist
    cluster = artist_row['cluster'].iloc[0]
    topic_label = artist_row['topic_label'].iloc[0]
    genre_label = artist_row['genre_label'].iloc[0]
    frequent_words = artist_row['frequent_words'].iloc[0]

    # Create a sample of 5 recommendations
    artist_sample = data[(data.cluster == cluster) & (data.artist != artist)].sample(5)
    artist_list = [row['artist'] for i, row in artist_sample.iterrows()]
    song_sample = pd.DataFrame()
    for i in range(0,5):
        song_sample = song_sample.append(original_data[original_data.artist == artist_list[i]].sample(1))
    resulting_dict = song_sample.to_dict(orient='index')

    new_data = {
        'topic_label': topic_label,
        'genre_label': genre_label,
        'frequent_words': frequent_words,
        'artist': initial_artist
    }
    resulting_dict['new_data'] = new_data
    return resulting_dict

def save_results(results):
    with open(os.path.join(APP_ROOT, 'evaluations.csv'), 'r+b') as f:
        header = next(csv.reader(f))
        dict_writer = csv.DictWriter(f, header, -999)
        dict_writer.writerow(results)
