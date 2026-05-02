import streamlit as st
from services.movie_service import load_movies, load_categories
from ui.filters import filter_category, filter_duration
from ui.modals import show_movie_info
from utils.preprocess import clean_duration


st.title("🎬 Netflix Movie Recommender", text_alignment="center")

df_movies = load_movies()
df_categories = load_categories()

categoria_seleccionada = filter_category(df_categories['categoria'])
duration = filter_duration()

if categoria_seleccionada:
    df_movies = clean_duration(df_movies)
    
    df = df_movies[
    (df_movies['listed_in'].str.contains(categoria_seleccionada, case=False, na=False)) &
    (df_movies['duration_int'] <= duration)
    ]
    
    if not df.empty:
        cols = st.columns(2)
        for i,(_,movie) in enumerate(df.iterrows()):
            with cols[i % 2]:
                with st.container(border = True):
                    st.image("https://images.pond5.com/white-line-cinema-camera-icon-footage-161363944_iconl.jpeg", width="stretch")
                    st.subheader(
                        movie["title"][:20] + "..." if len(movie["title"]) > 20 else movie["title"]
                    )
                    
                    st.write(f"🎬 Director: ", movie['director'][:20] + "..." if len(movie["director"]) > 20 else movie["title"])
                    st.write(f"⏱️ Duration: {movie['duration']} ")
                    
                    if st.button("View", key=f"btn_{i}"):
                        show_movie_info(movie)
    
    else:
        st.toast("No encontramos ninguna pelicula", icon="😢")

