import streamlit as st
import pickle
import pandas as pd
import requests
import os

# File ID from your shared Google Drive link
FILE_ID = '1qQhvOQEtzdCkDvTRLIXfR1J4fXGh9qdC'
DESTINATION = 'similarity.pkl'

# Safe download for large files from Google Drive
def download_file_from_google_drive(file_id, destination):
    def get_confirm_token(response):
        for key, value in response.cookies.items():
            if key.startswith('download_warning'):
                return value
        return None

    def save_response_content(response, destination):
        CHUNK_SIZE = 32768
        with open(destination, 'wb') as f:
            for chunk in response.iter_content(CHUNK_SIZE):
                if chunk:
                    f.write(chunk)

    if not os.path.exists(destination):
        URL = "https://docs.google.com/uc?export=download"
        session = requests.Session()

        response = session.get(URL, params={'id': file_id}, stream=True)
        token = get_confirm_token(response)

        if token:
            params = {'id': file_id, 'confirm': token}
            response = session.get(URL, params=params, stream=True)

        save_response_content(response, destination)

# Download the file if needed
download_file_from_google_drive(FILE_ID, DESTINATION)

# Load data
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Streamlit UI
st.title("🎬 Movie Recommendation System")

selected_movie_name = st.selectbox(
    'Select a movie to get recommendations:',
    movies['title'].values
)

# Recommend function
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(
        list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1]
    )
    recommended_movies = []
    for i in distances[1:6]:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

if st.button("Recommend"):
    st.subheader("Top 5 Recommendations:")
    recommendations = recommend(selected_movie_name)
    for i, name in enumerate(recommendations, 1):
        st.write(f"{i}. {name}")
