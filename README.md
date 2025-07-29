🎬 Movie Recommendation System
A Personalized Movie Recommendation Engine built using Python, Pandas, and Collaborative Filtering, deployed on Heroku.
This system predicts and recommends movies based on user preferences and movie similarities using the TMDB Movie Dataset.

🚀 Features
Personalized Recommendations

Suggests movies tailored to a user's past preferences.

Collaborative Filtering Algorithm

Computes similarity scores using adjusted cosine similarity.

Interactive Web App (Heroku)

Simple UI for entering a movie name and getting top similar movie recommendations.

Dataset from TMDB

Cleaned and preprocessed for high-quality recommendations.

🛠️ Tech Stack
Language: Python 3.x

Libraries: Pandas, NumPy, Scikit-learn, Streamlit

Dataset: TMDB Movie Dataset

Deployment: Heroku

📂 Project Structure
kotlin
Copy
Edit
Movie-Recommender-System/
├── app.py
├── data/
│   └── tmdb_movies.csv
├── model/
│   ├── similarity.pkl
│   └── movies.pkl
├── notebooks/
│   └── recommender.ipynb
├── requirements.txt
├── Procfile
└── README.md

Edit
streamlit run app.py
Access in Browser

Navigate to http://localhost:8501

