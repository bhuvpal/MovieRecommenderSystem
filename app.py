import streamlit as st
import pickle
import requests

cs = pickle.load(open('cs.pkl','rb'))
movie_df = pickle.load(open('movies.pkl','rb'))
movie_list = movie_df['title'].values



st.set_page_config('MovieRecommenderSystem')
st.title('Movie Recommender System')
selected_movie = st.selectbox('Select Movie',movie_list)


def fetch_poster(id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=5b51eecb3a7ba131dcb4fce71de88089'.format(id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def recommend(movie_name):
    index = movie_df[movie_df['title']==movie_name].index[0]
    distances = cs[index]
    recommend1 = sorted(list(enumerate(cs[index])),reverse=True,key=lambda x:x[1])[1:6]
    recommend2 = []
    recommend_poster = []
    for i in recommend1:
        id = movie_df.iloc[i[0]].id
        
        recommend2.append(movie_df.iloc[i[0]].title)
        recommend_poster.append(fetch_poster(id))
    return recommend2,recommend_poster

if st.button('Recommend'):
    recommendation,posters = recommend(selected_movie)

    col1,col2,col3,col4,col5 = st.columns(5)

    with col1:
         st.text(recommendation[0])
         st.image(posters[0])
    with col2:
         st.text(recommendation[1])
         st.image(posters[1])
    with col3:
         st.text(recommendation[2])
         st.image(posters[2])
    with col4:
         st.text(recommendation[3])
         st.image(posters[3])
    with col5:
         st.text(recommendation[4])
         st.image(posters[4])