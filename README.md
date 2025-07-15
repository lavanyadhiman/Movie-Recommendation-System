# Movie Recommendation System

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://lavanyadhiman-movie-recommendation-system-app-vcymho.streamlit.app/)

A content-based movie recommendation system built with Python and Streamlit. Select a movie, and the app will suggest five other movies with similar characteristics based on their genre, keywords, cast, and crew.

Movie Recommender Demo <img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/2488626d-cec8-484e-b14e-9149e4c2af6c" />


---

## Features

-   **Interactive Movie Selection:** Choose from a dropdown list of nearly 5,000 movies.
-   **Instant Recommendations:** Get a list of the top 5 similar movies instantly.
-   **Content-Based Filtering:** Recommendations are based on a comprehensive analysis of movie metadata, not just user ratings.
-   **Dynamic File Handling:** The application automatically downloads the necessary model file from Google Drive if it's not present locally.

---

## How It Works

This recommender system uses a **content-based filtering** approach. The core idea is to recommend items that are similar to those a user liked in the past.

1.  **Data Preprocessing:** Key metadata from the dataset (genres, overview, keywords, cast, and crew) are combined into a single "tags" string for each movie.
2.  **Text Vectorization:** The text in the "tags" for all movies is converted into a numerical format using `CountVectorizer`. This process creates a vector for each movie based on a vocabulary of the 5,000 most frequent words.
3.  **Similarity Calculation:** The **cosine similarity** is calculated between the vector of the selected movie and all other movies. Cosine similarity measures the cosine of the angle between two vectors, which indicates how similar they are.
4.  **Recommendation:** The top 5 movies with the highest cosine similarity scores (excluding the selected movie itself) are returned as recommendations.

---

## Dataset

This project uses the **TMDB 5000 Movie Dataset**, which is publicly available on Kaggle. It contains metadata for approximately 5,000 movies from The Movie Database (TMDb).

-   **Source:** [TMDB 5000 Movie Dataset on Kaggle](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)
-   **Content:** The dataset includes two main files:
    -   `tmdb_5000_movies.csv`: Contains movie details like budget, genres, keywords, overview, release date, etc.
    -   `tmdb_5000_credits.csv`: Contains cast and crew information for each movie.

---

## Tech Stack

-   **Language:** Python 3
-   **Web Framework:** Streamlit
-   **Machine Learning/NLP:** Scikit-learn
-   **Data Manipulation:** Pandas, NumPy
-   **File Handling:** Pickle, Requests

---

## Setup & Run Locally

To run this application on your local machine, follow these steps:

**1. Clone the Repository**

```bash
git clone https://github.com/lavanyadhiman/movie-recommendation-system.git
cd movie-recommendation-system
```

**2. Create a Virtual Environment (Recommended)**

```bash
# For Windows
python -m venv venv
venv\Scripts\activate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

**3. Install Dependencies**

Create a `requirements.txt` file with the following content:

```
streamlit
pandas
scikit-learn
requests
```

Then, run the installation command:

```bash
pip install -r requirements.txt
```

**4. Obtain Model Files**

You will need the `movie_dict.pkl` and `similarity.pkl` files. The application is designed to download `similarity.pkl` from Google Drive automatically. Ensure `movie_dict.pkl` is in the root directory.

**5. Run the Streamlit App**

```bash
streamlit run app.py
```

Your web browser should automatically open a new tab with the running application.

---

## Project Structure

```
.
├── movie_dict.pkl          # Serialized dictionary of movie data
├── similarity.pkl          # Pre-computed cosine similarity matrix (downloaded automatically)
├── app.py                  # The main Streamlit application script
├── requirements.txt        # Project dependencies
└── README.md               # You are here!
```

---

## Acknowledgements

This dataset was generated from The Movie Database (TMDb) API. This product uses the TMDb API but is not endorsed or certified by TMDb.
