import streamlit as st
import pickle
import pandas as pd
page_bg_img = """
<style>
[data-testid = "stAppViewContainer"] {
background-color: #9011c9;
opacity: 0.8;
background-image: radial-gradient(circle at center center, #25de45, #9011c9), repeating-radial-gradient(circle at center center, #25de45, #25de45, 4px, transparent 8px, transparent 4px);
background-blend-mode: multiply;
</style>
"""
st.title(':red[What movie do you want to watch?]')

st.markdown(page_bg_img, unsafe_allow_html=True)
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])[1:6]
    r_movies = []
    for i in distances:
        r_movies.append(movies.iloc[i[0]].title)
        movie_id = i[0]

    return r_movies

movies_dict = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl','rb'))



selected_movie_name = st.selectbox(
    ':red[Select Movie (Type or Choose)]',
    movies['title'].values)

if st.button('Recommend'):
   recommendations =  recommend(selected_movie_name)
   for i in recommendations:
     st.write(i)