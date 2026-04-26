# preprocessing.py

import pandas as pd
import ast
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords

ps = PorterStemmer()
stop_words = set(stopwords.words('english'))


def stem(text):
    y = []
    for i in text.split():
        if i not in stop_words:
            y.append(ps.stem(i))
    return " ".join(y)


def convert(text):
    L = []
    for i in ast.literal_eval(text):
        L.append(i['name'])
    return L


def convert3(text):
    L = []
    counter = 0
    for i in ast.literal_eval(text):
        if counter != 3:
            L.append(i['name'])
            counter += 1
        else:
            break
    return L


def fetch_director(text):
    L = []
    for i in ast.literal_eval(text):
        if i['job'] == 'Director':
            L.append(i['name'])
            break
    return L


def load_and_preprocess_data(movies_path, credits_path):

    # -----------------------------
    # Hollywood Dataset
    # -----------------------------
    movies = pd.read_csv(movies_path)
    credits = pd.read_csv(credits_path)

    movies = movies.merge(credits, on='title')

    movies = movies[['movie_id','title','overview','genres','keywords','cast','crew']]

    movies.dropna(inplace=True)

    movies['genres'] = movies['genres'].apply(convert)
    movies['keywords'] = movies['keywords'].apply(convert)
    movies['cast'] = movies['cast'].apply(convert3)
    movies['crew'] = movies['crew'].apply(fetch_director)

    movies['overview'] = movies['overview'].apply(lambda x:x.split())

    movies['genres'] = movies['genres'].apply(lambda x:[i.replace(" ","") for i in x])
    movies['keywords'] = movies['keywords'].apply(lambda x:[i.replace(" ","") for i in x])
    movies['cast'] = movies['cast'].apply(lambda x:[i.replace(" ","") for i in x])
    movies['crew'] = movies['crew'].apply(lambda x:[i.replace(" ","") for i in x])

    movies['tags'] = movies['overview'] + movies['genres'] + movies['keywords'] + movies['cast'] + movies['crew']

    hollywood = movies[['title','tags']]
    hollywood['tags'] = hollywood['tags'].apply(lambda x:" ".join(x))

    data = hollywood


    # -----------------------------
    # Final Cleaning
    # -----------------------------
    data.dropna(inplace=True)

    data['tags'] = data['tags'].apply(lambda x: x.lower())
    data['tags'] = data['tags'].apply(stem)

    data.reset_index(drop=True, inplace=True)

    return data