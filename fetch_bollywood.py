# fetch_bollywood.py

import requests
import pandas as pd
import time

API_KEY ="3e46e6bfda78e4fbd608c59efbe6f30"

movies = []

for page in range(1, 20):  # fetch ~400 movies

    url = f"https://api.themoviedb.org/3/discover/movie?api_key={API_KEY}&with_original_language=hi&sort_by=popularity.desc&page={page}"

    response = requests.get(url).json()

    for movie in response['results']:

        movies.append({
            "title": movie['title'],
            "overview": movie['overview'],
            "genres": "",
            "keywords": "",
            "cast": "",
            "crew": ""
        })

    time.sleep(0.3)

df = pd.DataFrame(movies)

df.to_csv("bollywood_movies.csv", index=False)

print("Bollywood dataset created!")