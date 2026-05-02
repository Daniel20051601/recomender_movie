import streamlit as st
from services.movie_service import get_longest_duration,get_shortest_movie

longest_duration = int(get_longest_duration())
shortest_duration = int(get_shortest_movie())

def filter_category(categories):
    return st.selectbox(
        "Seleccione una categoria",
        categories,
        index=None,
        placeholder="Elija una opcion"
    )
    
def filter_duration():
    return st.slider("Duracion maxima", shortest_duration, longest_duration,80) 

