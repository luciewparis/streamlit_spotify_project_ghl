import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#st.set_page_config(page_title="Spotify Music Insights", layout="wide")

logo_url = "https://upload.wikimedia.org/wikipedia/commons/2/26/Spotify_logo_with_text.svg"


st.markdown(
    f"""
    <div style="display: flex; align-items: center; justify-content: center; gap: 15px;">
        <img src="{logo_url}" width="120">
        <h1 style="margin-bottom: 0;">Welcome to the Spotify Music Insights <br> <span style="display: block; text-align: center;">Dashboard</span></h1>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("### Contexte")

st.markdown(
     """
     **Spotify: The World's Leading Music Streaming Platform**  
    Launched in **2008**, Spotify has revolutionized the way people consume music by offering **on-demand streaming** with millions of songs, albums, and playlists.  
    Today, it is available in **over 180 countries**, connecting artists and listeners worldwide.  

     **Why Spotify Matters?**  
    - Over **700 million active users** (as of 2024).  
    - More than **265 million premium subscribers**.  
    - A vast library of **100+ million tracks** and **5M+ podcasts**.  
    - AI-driven **personalized recommendations** through algorithms and curated playlists.  
"""
)

st.markdown("### Spotify Top 10 Insights")
col1, col2 = st.columns(2)

# Top 10 Artists Data
top_artists_data = {
    'Artist': ['Bad Bunny', 'The Weeknd', 'Drake', 'Taylor Swift', 'Post Malone',
               'Ed Sheeran', 'Ariana Grande', 'MUSIC LAB JPN', 'Olivia Rodrigo', 'Eminem'],
    'Spotify Streams (in billions)': [37.05, 36.95, 34.96, 34.47, 26.14, 
                                      24.01, 23.46, 22.87, 19.73, 18.88]
}

# Top 10 Tracks Data
top_tracks_data = {
    'Track': ['Blinding Lights', 'Blinding Lights', 'Shape of You', 'Shape of You', 
              'Someone You Loved', 'Sunflower - Spider-Man: Into the Spider-Verse', 
              'As It Was', 'As It Was', 'Starboy', 'One Dance'],
    'Spotify Streams (in billions)': [4.28, 4.26, 3.91, 3.89, 3.43, 3.36, 3.30, 3.30, 3.29, 3.19]
}


top_artists_df = pd.DataFrame(top_artists_data)
top_tracks_df = pd.DataFrame(top_tracks_data)


top_artists_df['Spotify Streams (in billions)'] = top_artists_df['Spotify Streams (in billions)'].map(lambda x: f"{x:.2f}")
top_tracks_df['Spotify Streams (in billions)'] = top_tracks_df['Spotify Streams (in billions)'].map(lambda x: f"{x:.2f}")


top_artists_df = top_artists_df[['Artist', 'Spotify Streams (in billions)']]
top_tracks_df = top_tracks_df[['Track', 'Spotify Streams (in billions)']]



with col1:
    st.markdown("#### Top 10 Most Streamed Artists")
    st.dataframe(top_artists_df.style.set_properties(**{'background-color': 'lightgreen',
                                                        'color': 'black',
                                                        'border': '1px solid black',
                                                        'text-align': 'center'})
                 .applymap(lambda val: 'font-weight: bold', subset=['Artist']), use_container_width=True)


with col2:
    st.markdown("#### Top 10 Most Streamed Tracks")
    st.dataframe(top_tracks_df.style.set_properties(**{'background-color': 'lightgreen',
                                                        'color': 'black',
                                                        'border': '1px solid black',
                                                        'text-align': 'center'})
                 .applymap(lambda val: 'font-weight: bold', subset=['Track']), use_container_width=True)