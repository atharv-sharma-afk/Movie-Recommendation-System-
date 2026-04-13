# recommend.py

import pickle
import matplotlib.pyplot as plt
import seaborn as sns

movies = pickle.load(open("movies_clustered.pkl","rb"))
similarity = pickle.load(open("similarity.pkl","rb"))


def explain(movie1, movie2):

    tags1 = set(movies[movies['title']==movie1]['tags'].values[0].split())
    tags2 = set(movies[movies['title']==movie2]['tags'].values[0].split())

    common = tags1.intersection(tags2)

    return list(common)[:5]


def recommend(movie):

    movie_index = movies[movies['title'] == movie].index[0]

    cluster = movies.iloc[movie_index]['cluster']

    cluster_movies = movies[movies['cluster'] == cluster].index

    sim_scores = [(i, similarity[movie_index][i]) for i in cluster_movies]

    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:6]

    movie_indices = [i[0] for i in sim_scores]

    titles = movies.iloc[movie_indices]['title'].values
    scores = [i[1] for i in sim_scores]
    if len(sim_scores) < 5:
        print("Not enough similar movies found")

    print("\nRecommended Movies:\n")

    for t, s in zip(titles, scores):
        reason = explain(movie, t)
        print(f"{t}  | score={round(s,3)}")
        print("Why recommended:", reason)
        print()

    return titles, scores



recommend("Pirates of the Caribbean: At World's End")