# app.py

import streamlit as st
import pickle

movies = pickle.load(open("models/movies_clustered.pkl","rb"))
similarity = pickle.load(open("models/similarity.pkl","rb"))


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

    return titles, scores


st.title("🎬 Explainable Movie Recommender (ML Project)")
st.write("KMeans Clustering + Cosine Similarity")

selected_movie = st.selectbox(
    "Choose a movie",
    movies['title'].values
)

if st.button("Recommend"):

    titles, scores = recommend(selected_movie)

    for t, s in zip(titles, scores):

        reason = explain(selected_movie, t)

        st.subheader(t)
        st.write("Similarity Score:", round(s,3))
        st.write("Why Recommended:", reason)
        st.write("---")