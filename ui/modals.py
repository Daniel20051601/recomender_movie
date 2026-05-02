import streamlit as st
import ast

@st.dialog("Information")
def show_movie_info(Movie):
    cast = ", ".join(ast.literal_eval(Movie['cast']))
    col1, col2 = st.columns(2)
    col3, col4 = st.columns(2)
    with col1: 
        st.image("https://images.pond5.com/white-line-cinema-camera-icon-footage-161363944_iconl.jpeg", width="stretch")
         
    with col2:
        st.header(Movie['title'])
        st.write(f"🎬Director: {Movie['director']}")
        st.write(f"⏱️Duration: {Movie['duration']} ")

    with col3:
        st.subheader("🤵Cast")
        st.write(cast)
    
    with col4:
        st.subheader('🎞️Categories')
        print_badges_category(Movie)

def print_badges_category(Movie):
    categorias = ast.literal_eval(Movie['listed_in'])
    for category in categorias:
        st.badge(category)
