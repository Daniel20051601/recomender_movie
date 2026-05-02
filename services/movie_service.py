import pandas as pd
from database.conection import get_engine
from database.movies_querys import get_categories, get_movies
from utils.preprocess import clean_categories, clean_duration

engine = get_engine()

def load_movies():
    return get_movies()

def load_categories():
    df = get_categories()
    return clean_categories(df)

def get_longest_duration():
    df_movies_with_durationint = clean_duration(load_movies())
    longest_movie = df_movies_with_durationint.loc[df_movies_with_durationint['duration_int'].idxmax()]
    
    return  longest_movie['duration_int']

def get_shortest_movie():
    df_movies_with_durationint = clean_duration(load_movies())
    shortest_movie = df_movies_with_durationint.loc[df_movies_with_durationint['duration_int'].idxmin()]
    
    return shortest_movie['duration_int'] 
       