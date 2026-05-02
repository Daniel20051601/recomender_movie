from database.conection import get_engine
import pandas as pd

engine = get_engine()

def get_movies():
    return pd.read_sql('SELECT * FROM "Movies"', engine)
    
def get_categories():
    return pd.read_sql('SELECT * FROM "categoria"', engine)

    