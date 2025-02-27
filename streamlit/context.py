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
    oday, it is available in over 180 countries, connecting artists and listeners worldwide, with the majority of users based in the United States.  

     **Why Spotify Matters?**  
    - Over **700 million active users** (as of 2024).  
    - More than **265 million premium subscribers**.  
    - A vast library of **100+ million tracks** and **5M+ podcasts**.  
    - AI-driven **personalized recommendations** through algorithms and curated playlists.  
"""
)

st.markdown("### Spotify Top 10 Insights")

file_path_main = "./data/Merged_Spotify_Data_with_region_spotyfolow_markets.csv"
df_main = pd.read_csv(file_path_main)


df_main = df_main.drop_duplicates()

top_tracks_final = df_main[['Track', 'Spotify Streams']]\
    .groupby('Track', as_index=False).sum()\
    .sort_values(by='Spotify Streams', ascending=False)\
    .head(10)

top_artists_final = df_main[['Artist', 'Spotify Streams']]\
    .groupby('Artist', as_index=False).sum()\
    .sort_values(by='Spotify Streams', ascending=False)\
    .head(10)

# Convertir les streams en milliards et arrondir à 2 décimales
top_tracks_final['Spotify Streams (Billions)'] = (top_tracks_final['Spotify Streams'] / 1e9).round(2)
top_artists_final['Spotify Streams (Billions)'] = (top_artists_final['Spotify Streams'] / 1e9).round(2)

top_tracks_final = top_tracks_final[['Track', 'Spotify Streams (Billions)']]
top_artists_final = top_artists_final[['Artist', 'Spotify Streams (Billions)']]

col1, col2 = st.columns(2)

with col1:
    st.subheader("Top 10 Tracks 🎶")
    st.dataframe(top_tracks_final, use_container_width=True)

with col2:
    st.subheader("Top 10 Artistes 🎤")
    st.dataframe(top_artists_final, use_container_width=True)
