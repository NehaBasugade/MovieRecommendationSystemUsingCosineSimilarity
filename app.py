import streamlit as st
import pickle
import pandas as pd
import movieposters as mp
import urllib
from PIL import Image

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movie=[]
    for i in movies_list:
        movie_id=i[0]
        #fetch poster 
        recommended_movie.append(movies.iloc[i[0]].title + " - " + movies.iloc[i[0]].genre)
    return recommended_movie

movies_dict=pickle.load(open('./Weights/movie_dict (2).pkl','rb'))
movies=pd.DataFrame(movies_dict)

similarity=pickle.load(open('./Weights/similarity .pkl','rb'))

st.title("Movie Recommender System")

selected_movie_name=st.selectbox('How would you like to be connected? ',movies['title'].values)

if st.button('Recommend'):
    recommendations=recommend(selected_movie_name)
    for i in recommendations:
     a = i.split(" -")
     a = a[0]
     link = mp.get_poster(title=a)
     urllib.request.urlretrieve(link,'poster.png')
     img = Image.open('poster.png')
     st.image(img,width=150)
     st.write(i)