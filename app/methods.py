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

def predict_cluster(lyrics):

    # Get dataframes and clusters
    data = pd.read_pickle(os.path.join(APP_STATIC, 'data/clustered_lyrics.pkl'))
    original_data = pd.read_pickle(os.path.join(APP_STATIC, 'data/clustered_lyrics.pkl'))
    km = joblib.load(os.path.join(APP_STATIC, 'data/doc_cluster_big.pkl'))

    # Build vocabulary of existing clusters
    vectorizer = TfidfVectorizer(
        ngram_range=(1, 1),
        stop_words='english',
        min_df=25,
        max_df=0.5
    )
    x = vectorizer.fit_transform(data['lyrics_string'])
    vocabulary = vectorizer.get_feature_names()

    # Clean lyrics and build new entry
    new_data = {
        "artist": "new",
        "cluster": 0,
        "frequent_words": "",
        "x": 0,
        "y": 0
    }

    brackets_regex = re.compile('\[.*?\]')
    apostrophe_regex = re.compile("[']")
    punctuation_regex = re.compile('[^0-9a-zA-Z ]+')
    double_space_regex = re.compile('\s+')

    initial_lyrics = lyrics
    lyrics = initial_lyrics.lower()
    lyrics = brackets_regex.sub("", lyrics)
    lyrics = apostrophe_regex.sub("", lyrics)
    lyrics = punctuation_regex.sub("", lyrics)
    lyrics = double_space_regex.sub(" ", lyrics)
    lyrics = lyrics.split()
    lyrics = [word for word in lyrics if word in vocabulary]
    lyrics = ' '.join(lyrics)
    new_data['lyrics_string'] = lyrics
    new_data = pd.DataFrame(new_data, index=[len(data)])
    data = data.append(new_data)

    # Create TF-IDF matrix with new data and predict cluster
    x = vectorizer.fit_transform(data['lyrics_string'])
    features = vectorizer.get_feature_names()
    predictions = km.predict(x)
    cluster = predictions[-1]
    topic_label = data[data.cluster == cluster].iloc[0]['topic_label']
    genre_label = data[data.cluster == cluster].iloc[0]['genre_label']
    frequent_words = data[data.cluster == cluster].iloc[0]['frequent_words']

    # Create a sample of 5 recommendations
    artist_sample = data[(data.cluster == cluster) & (data.artist != 'new')].sample(5)
    artist_list = [row['artist'] for i, row in artist_sample.iterrows()]
    song_sample = pd.DataFrame()
    for i in range(0,5):
        song_sample = song_sample.append(original_data[original_data.artist == artist_list[i]].sample(1))
    resulting_dict = song_sample.to_dict(orient='index')

    new_data = {
        'topic_label': topic_label,
        'genre_label': genre_label,
        'frequent_words': frequent_words,
        'lyrics': initial_lyrics
    }
    resulting_dict['new_data'] = new_data
    return resulting_dict

def save_results(results):
    with open(os.path.join(APP_ROOT, 'evaluations.csv'), 'r+b') as f:
        header = next(csv.reader(f))
        dict_writer = csv.DictWriter(f, header, -999)
        dict_writer.writerow(results)
