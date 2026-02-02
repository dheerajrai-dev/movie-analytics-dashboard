import pandas as pd
import streamlit as st

@st.cache_data
def load_data():
    """
    Loads the cleaned movie data efficiently.
    Used by app.py to get the dataframe.
    """
    try:
        # Load the clean dataset
        df = pd.read_csv("data/movies_cleaned.csv")
        
        # Ensure text columns are handled correctly (fill missing with empty string)
        df['overview'] = df['overview'].fillna("No summary available.")
        df['main_actors'] = df['main_actors'].fillna("")
        
        return df
        
    except FileNotFoundError:
        # Returns an empty dataframe if the file is missing
        return pd.DataFrame()