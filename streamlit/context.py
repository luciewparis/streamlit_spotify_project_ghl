import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# Set page title
# st.set_page_config(page_title="Spotify Music Insights", layout="wide")

# Spotify logo URL
logo_url = "https://upload.wikimedia.org/wikipedia/commons/2/26/Spotify_logo_with_text.svg"

# Welcome Message with Centered "Dashboard"
st.markdown(
    f"""
    <div style="display: flex; align-items: center; justify-content: center; gap: 15px;">
        <img src="{logo_url}" width="120">
        <h1 style="margin-bottom: 0;">Welcome to the Spotify Music Insights <br> <span style="display: block; text-align: center;">Dashboard</span></h1>
    </div>
    """,
    unsafe_allow_html=True
)

# Header
st.markdown("### Contexte")

# Context Section
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

     **Impact on the Music Industry**  
    Spotify has transformed music consumption, enabling artists to reach a **global audience** while shaping industry trends through **streaming analytics, playlist curation, and viral discoveries on social media platforms**.
    """
)

st.markdown("### Key Spotify Figures")
st.markdown("#### Tracking Monthly Active Users & Premium Subscribers Over Time")

# Context
st.markdown(
    """
    Spotify has become the **leading music streaming platform** with continuous growth in **monthly active users (MAUs) and premium subscribers**.
    This graph illustrates the **evolution from 2011 to 2024**, showcasing Spotify’s impact on the global music industry.
    """
)

#source (https://www.statista.com/chart/15697/spotify-user-growth/)
years = np.arange(2011, 2025) 
monthly_active_users = [5, 10, 20, 30, 50, 75, 100, 150, 200, 250, 300, 400, 550, 678]  # 14 values
premium_subscribers = [2, 5, 10, 15, 25, 40, 60, 80, 100, 140, 180, 220, 250, 265]  # 14 values


fig, ax = plt.subplots(figsize=(10, 6))

# Plot the data
ax.plot(years, monthly_active_users, marker='o', linestyle='-', label="Monthly Active Users")
ax.plot(years, premium_subscribers, marker='o', linestyle='-', color='darkgreen', label="Premium Subscribers")

# Annotate last data points
ax.text(2024, 678, "Dec. '24\n678M", verticalalignment='bottom', fontsize=10, fontweight='bold')
ax.text(2024, 265, "Dec. '24\n265M", verticalalignment='bottom', color='darkgreen', fontsize=10, fontweight='bold')

# Titles and labels
ax.set_title("Spotify Growth: Monthly Active Users & Premium Subscribers", fontsize=14, fontweight='bold')
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Users (in Millions)", fontsize=12)
ax.set_xticks(np.arange(2011, 2025, step=2))
ax.set_yticks(np.arange(0, 750, step=100))
ax.legend()
ax.grid(True, linestyle='--', alpha=0.6)

st.pyplot(fig)



