import streamlit as st
import pickle
import pandas as pd
import requests
import os

def download_file_from_google_drive(file_id, destination):
    if not os.path.exists(destination):
        url = f"https://drive.google.com/uc?id={file_id}"
        r = requests.get(url)
        with open(destination, 'wb') as f:
            f.write(r.content)

# File ID from your shared Google Drive link
file_id = '1qQhvOQEtzdCkDvTRLIXfR1J4fXGh9qdC'
download_file_from_google_drive(file_id, 'similarity.pkl')

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
