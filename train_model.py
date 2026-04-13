# train_model.py

import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns

from preprocessing import load_and_preprocess_data


# Load data
movies = load_and_preprocess_data(
    "tmdb_5000_movies.csv",
    "tmdb_5000_credits.csv"
)


tfidf = TfidfVectorizer(
    max_features=5000,
    stop_words='english',
    ngram_range=(1,2)
)

vectors = tfidf.fit_transform(movies['tags']).toarray()

# Cosine similarity
similarity = cosine_similarity(vectors)

# ---------------------------
# KMeans Clustering (ML MODEL)
# ---------------------------

K = 8

kmeans = KMeans(n_clusters=K, random_state=42)
movies['cluster'] = kmeans.fit_predict(vectors)

# ---------------------------
# Evaluation (Silhouette Score)
# ---------------------------

score = silhouette_score(vectors, movies['cluster'])
print("Silhouette Score:", score)

# ---------------------------
# PCA Visualization
# ---------------------------

pca = PCA(n_components=2)
reduced = pca.fit_transform(vectors)

plt.figure(figsize=(10,8))
sns.scatterplot(x=reduced[:,0], y=reduced[:,1], hue=movies['cluster'], palette="viridis")
plt.title("Movie Clusters using KMeans")
plt.savefig("clusters_pca.png")
plt.show()

# ---------------------------
# Save Models
# ---------------------------

pickle.dump(movies, open("movies_clustered.pkl","wb"))
pickle.dump(similarity, open("similarity.pkl","wb"))
pickle.dump(kmeans, open("kmeans_model.pkl","wb"))

print("Models saved successfully!")