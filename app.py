import streamlit as st
import pickle
import pandas as pd
import requests
import gdown
import os



MOVIES_FILE_ID = "https://drive.google.com/file/d/1l1E8VsQdMyxMumP0Y_xjsmqe8L9TW7i5/view?usp=drive_link"
SIMILARITY_FILE_ID = "https://drive.google.com/file/d/11inXxpuItE9VtNAzWideUADMTzMewVvT/view?usp=drive_link"

# Download movies_dict.pkl if not exists
if not os.path.exists("movies_dict.pkl"):
    gdown.download(f"https://drive.google.com/uc?export=download&id={MOVIES_FILE_ID}", "movies_dict.pkl", quiet=False)

# Download similarity.pkl if not exists
if not os.path.exists("similarity.pkl"):
    gdown.download(f"https://drive.google.com/uc?export=download&id={SIMILARITY_FILE_ID}", "similarity.pkl", quiet=False)

movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))




def fetch_poster(movie_id):
    response = requests.get(
        f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=0d60b6817dd765ff09d5aa2cb588af63&language=en-US'
    )
    data = response.json()
    return "http://image.tmdb.org/t/p/w500/" + data['poster_path']

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_poster = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_poster.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_poster

st.title('🎬 Movie Recommender System')

selected_movie = st.selectbox("Select a Movie", movies['title'].values)

if st.button('Recommend'):
    names, poster = recommend(selected_movie)

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(poster[0])
    with col2:
        st.text(names[1])
        st.image(poster[1])
    with col3:
        st.text(names[2])
        st.image(poster[2])
    with col4:
        st.text(names[3])
        st.image(poster[3])
    with col5:
        st.text(names[4])
        st.image(poster[4])
