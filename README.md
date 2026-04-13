🎬 Explainable Movie Recommendation System using KMeans + TF-IDF

A Machine Learning based Explainable Movie Recommendation System that suggests similar movies using TF-IDF vectorization, KMeans clustering, and Cosine Similarity, with a Streamlit UI.

The system also explains why a movie was recommended using common keywords.

🚀 Features
TF-IDF based text vectorization
KMeans clustering (ML model)
Cosine similarity recommendation
Explainable AI (why recommended)
Similarity score display
PCA cluster visualization
Streamlit interactive UI
Modular project structure
🧠 ML Pipeline
Movie Dataset
     ↓
Data Preprocessing
     ↓
Stopword Removal + Stemming
     ↓
TF-IDF Vectorization
     ↓
KMeans Clustering (ML Model)
     ↓
Cosine Similarity
     ↓
Explainable Recommendations
     ↓
Streamlit UI
📂 Project Structure
Movie_Recommender
│
├── app.py
├── recommend.py
├── train_model.py
├── preprocessing.py
│
├── movies_clustered.pkl
├── similarity.pkl
├── kmeans_model.pkl
├── clusters_pca.png
│
├── tmdb_5000_movies.csv
├── tmdb_5000_credits.csv
│
└── README.md
⚙️ Technologies Used
Python
Scikit-learn
TF-IDF Vectorizer
KMeans Clustering
Cosine Similarity
NLTK (stopwords + stemming)
Streamlit
Pandas
NumPy
Matplotlib / Seaborn
📊 Machine Learning Models Used
1. TF-IDF Vectorizer

Converts movie tags into numerical feature vectors while reducing importance of common words.

2. KMeans Clustering

Groups similar movies into clusters.

Movies are recommended within the same cluster.

3. Cosine Similarity

Finds most similar movies using vector angle similarity.

4. PCA (Visualization)

Reduces dimensionality to visualize movie clusters.

📈 Similarity Formula

Cosine similarity:

𝑠
𝑖
𝑚
𝑖
𝑙
𝑎
𝑟
𝑖
𝑡
𝑦
=
𝐴
⋅
𝐵
∣
∣
𝐴
∣
∣
∣
∣
𝐵
∣
∣
similarity=
∣∣A∣∣∣∣B∣∣
A⋅B
	​


Range:

1 → Highly similar
0 → Not similar
💡 Explainable Recommendation

System shows:

similarity score
common keywords
same cluster movies

Example:

Avatar

Recommended:
Avengers
Score: 0.82
Why: action, space, hero, battle
▶️ How to Run
Step 1 — Install dependencies
pip install pandas numpy scikit-learn nltk streamlit seaborn matplotlib
Step 2 — Train Model
python train_model.py

This will generate:

similarity.pkl
movies_clustered.pkl
kmeans_model.pkl
clusters_pca.png
Step 3 — Run Streamlit App
streamlit run app.py
📊 Dataset

TMDB 5000 Movie Dataset

Files used:

tmdb_5000_movies.csv
tmdb_5000_credits.csv
🎯 Project Objective

To build an Explainable Movie Recommendation System using machine learning techniques that:

improves recommendation accuracy
uses clustering
explains recommendations
provides interactive UI
📌 Example Output

Input:

Avatar

Output:

Avengers
Score: 0.82
Why: action, hero, space

Guardians of the Galaxy
Score: 0.79
Why: space, team, adventure
📉 Cluster Visualization

Clusters generated using KMeans and visualized using PCA

See:

clusters_pca.png
👨‍💻 Author

Atharv Sharma
B.Tech CSE (Data Science)
Machine Learning Project – Semester 6