import pandas as pd
import streamlit as st
import pickle


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movie_list:
        movie_id = movies.iloc[i[0]].id
        recommended_movies.append(movies['title'].iloc[i[0]])
    return recommended_movies

movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)


similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Movie Recommender System')

selected_movie_name  = st.selectbox(
    'Which Movie recommendations would you like to see?',
    movies['title'].values
)


if st.button('Recommend'):
    names  = recommend(selected_movie_name)
    for name in names:
        st.write(name)

