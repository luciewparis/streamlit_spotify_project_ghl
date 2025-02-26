import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import ast
from collections import Counter 
#
# st.markdown(
   # "<h1 style='text-align: center;'> Which selection of artists will ensure the success of a music festival?</h1>",
    #unsafe_allow_html=True,
#)
st.title("Which selection of artists will ensure the success of a music festival?")


tab1, tab2, tab3 = st.tabs(["     Introduction     ", 
                                  "     Analysis Factors     ", 
                                  "     Conclusion     "])

# === Introduction ===
with tab1:
    st.markdown("## Introduction")
    st.write(
        """
        The selection of artists is a key factor in the success of a music festival. However, several criteria must be considered to 
        ensure a lineup that attracts a broad audience and generates strong engagement.

        In this analysis, we focused on four main dimensions based on data from our dataset:

        - **Popularity**
        - **Virality and Social Impact**
        - **Geographical Influence**
        - **Diversity and Adaptability**
        """
    )
    image_path = "./streamlit/images/image_festival.jpg" 
    st.image(image_path, use_container_width=True) 
    #st.image(image_path, use_column_width=True)
    
# === Analysis Factors ===
with tab2:
    st.markdown("## Analysis Factors")
    
    st.markdown("### Popularity")  
    st.markdown("#### 1- Top Spotify Artists") 
    file_path = "./data/cleaned_Spotify_Songs_2024.csv" 
    
    
    try:
        data_cleaned = pd.read_csv(file_path, encoding='latin1')
    except FileNotFoundError:
        st.error("Le fichier CSV n'a pas été trouvé. Vérifiez le chemin d'accès.")
        st.stop()
    
    # Total stream per artist 
    top_artists = data_cleaned.groupby('Artist')['Spotify Streams'].sum().reset_index()
    top_artists = top_artists.sort_values(by='Spotify Streams', ascending=False).head(10)

    # Add number of tracks per artist 
    artist_track_count = data_cleaned.groupby("Artist")["Track"].count().reset_index()
    artist_track_count = artist_track_count.rename(columns={'Track': 'Number of Tracks'})

    # Merge
    top_artists = top_artists.merge(artist_track_count, on="Artist", how="left")

    
    fig, ax = plt.subplots(figsize=(12, 6))
    cmap = sns.color_palette("Blues", as_cmap=True)
    
    bars = ax.bar(top_artists["Artist"], 
                  top_artists["Spotify Streams"], 
                  color=cmap(top_artists["Number of Tracks"] / top_artists["Number of Tracks"].max()))
    
    ax.set_xlabel("Artists")
    ax.set_ylabel("Stream Volume")
    ax.set_title("TOP 10 Most Listened Artists in the World")
    ax.set_xticklabels(top_artists["Artist"], rotation=45, ha='right')
    
    sm = plt.cm.ScalarMappable(cmap=sns.color_palette("Blues", as_cmap=True), 
                               norm=plt.Normalize(vmin=top_artists["Number of Tracks"].min(), 
                                                  vmax=top_artists["Number of Tracks"].max()))
    cbar = fig.colorbar(sm, ax=ax)
    cbar.set_label("Number of Tracks")
    st.pyplot(fig)
    

    
    st.markdown("""

    #### 🔍 **Key Insights:**  
    - **Most Popular Artists**: Bad Bunny, The Weeknd, Drake, and Taylor Swift lead in streaming volume.  
    - **Correlation Between Tracks and Popularity**: Artists with a higher number of tracks tend to have higher streaming volumes.  
    - **Significant Disparity**: The top four artists have a noticeable gap compared to the rest of the ranking.  
    - **Strategy for a Music Festival**: Booking these artists could maximize audience attendance and engagement.  
 
    """)
    st.markdown("#### 2- Popular Artists")  
    st.markdown(""" 
    The Popularity Score is a composite metric that quantifies an artist's overall popularity by combining Spotify Popularity, Spotify Streams, YouTube Views, TikTok Views, and Shazam Counts, with each metric scaled appropriately. It provides a unified measure to compare artists across multiple platforms based on streaming and engagement data.
    """)
    # Calculation of popularity score by combining multiple sources
    data_cleaned["Popularity Score"] = (
        data_cleaned["Spotify Popularity"].fillna(0) + 
        data_cleaned["Spotify Streams"].fillna(0) / 1e6 + 
        data_cleaned["YouTube Views"].fillna(0) / 1e6 +
        data_cleaned["TikTok Views"].fillna(0) / 1e6 + 
        data_cleaned["Shazam Counts"].fillna(0) / 1e5   
    )

    top_artists = data_cleaned.groupby("Artist")["Popularity Score"].sum().sort_values(ascending=False).head(10)

    fig, ax = plt.subplots(figsize=(12, 6))
    top_artists.plot(kind='bar', ax=ax)
    ax.set_xlabel("Artists")
    ax.set_ylabel("Popularity Score")
    ax.set_title("Top 10 Most Popular Artists (2024)")
    ax.set_xticklabels(top_artists.index, rotation=45, ha='right')  
    st.pyplot(fig)
    st.markdown("""

    #### 🔍 **Key Insights:**  
    - **Different Rankings**: The most streamed artists are not necessarily the most popular across all platforms.
    - **Unexpected Leaders**: Kevin MacLeod and The King Khan & BBQ Show rank highest due to engagement beyond traditional streaming.
    - **Mainstream Artists Still Strong**: Bad Bunny, Taylor Swift, and Drake maintain high popularity across platforms. 
    - **Multi-Platform Impact**: Popularity is driven by more than just streams—YouTube, TikTok, and Shazam also play a key role.
 
    """)
    st.markdown("### Virality and Social Impact")  
    st.markdown("#### 1- YouTube Views and Likes")  

    data_cleaned["YouTube Impact"] = (
        data_cleaned["YouTube Views"].fillna(0) / 1e6 +  
        data_cleaned["YouTube Likes"].fillna(0) / 1000
    )

    top_youtube_tracks = data_cleaned[["Track", "Artist", "YouTube Impact"]].sort_values(by="YouTube Impact", ascending=False).head(10)

    fig, ax = plt.subplots(figsize=(12, 6))
    ax.barh(top_youtube_tracks["Track"] + " - " + top_youtube_tracks["Artist"], top_youtube_tracks["YouTube Impact"])
    ax.set_xlabel("YouTube Impact (Views in Millions + Likes in Thousands)")
    ax.set_ylabel("Song - Artist")
    ax.set_title("Top 10 Most Popular Songs on YouTube")
    ax.invert_yaxis()  
    st.pyplot(fig)

    st.markdown("#### 2- TikTok Posts, Likes et Views") 

    # Calculate TikTok Impact Score
    data_cleaned["TikTok Impact"] = (
        data_cleaned["TikTok Posts"].fillna(0) +
        data_cleaned["TikTok Likes"].fillna(0) / 1000 +
        data_cleaned["TikTok Views"].fillna(0) / 1e6
    )

    top_tiktok_tracks = data_cleaned.sort_values(by="TikTok Impact", ascending=False).head(10)

    fig, ax = plt.subplots(figsize=(12, 6))
    ax.barh(top_tiktok_tracks["Track"] + " - " + top_tiktok_tracks["Artist"], top_tiktok_tracks["TikTok Impact"])
    ax.set_xlabel("TikTok Impact Score (Views in Millions + Likes in Thousands)")
    ax.set_ylabel("Track")
    ax.set_title("Top 10 Viral Songs on TikTok (2024)")
    ax.invert_yaxis()
    st.pyplot(fig)

    st.markdown("#### 3- Shazam Counts") 
    
    data_cleaned["Track_Artist"] = data_cleaned["Track"] + " - " + data_cleaned["Artist"]
    top_shazam = data_cleaned[["Track_Artist", "Shazam Counts"]].sort_values(by="Shazam Counts", ascending=False).head(10)
    #st.set_option('deprecation.showPyplotGlobalUse', False)
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.barh(top_shazam["Track_Artist"], top_shazam["Shazam Counts"])
    ax.set_xlabel("Shazam Search Count")
    ax.set_ylabel("Track - Artist")
    ax.set_title("Top 10 Songs by Shazam Search Count")
    ax.invert_yaxis()

    st.pyplot(fig)
    st.markdown("""

    #### 🔍 **Key Insights:**  
    - **YouTube Hits Drive Popularity**: Songs like Despacito and Dynamite dominate YouTube, proving that video engagement correlates with mainstream success.
    - **TikTok Virality is Trend-Based**: Tracks like Monkeys Spinning Monkeys and Love You So gain popularity through memes and challenges, not traditional streaming.
    - **Shazam Reflects Music Discovery**: High Shazam counts suggest songs frequently heard in real-world settings, indicating potential rising stars.
    - **Different Platforms, Different Impact**: YouTube, TikTok, and Shazam success don’t always align, showing varied audience behaviors.
 
    """)
       # 🔵 Geographic Influence
    st.markdown("### Geographic Influence")  
    file_path = "./data/Merged_Spotify_Data_with_region_spotyfolow_markets.csv"
    df = pd.read_csv(file_path, encoding="latin1")
    # Function to count available markets
    def count_markets(value):
        try:
            return len(ast.literal_eval(value)) if value != "Not found" else 0
        except:
            return 0

    df["track_markets_cleaned"] = df["track_markets"].apply(count_markets)

    artist_total_markets = (
    df.groupby("Artist")["track_markets_cleaned"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    )

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.barh(artist_total_markets.index[::-1], artist_total_markets[::-1])
    ax.set_xlabel("Total Number of Markets")
    ax.set_ylabel("Artists")
    ax.set_title("Top 10 Artists by Total Market Presence")
    ax.grid(axis='x', linestyle="--", alpha=0.7)
    st.pyplot(fig)

    st.markdown("""

    #### 🔍 **Key Insights:**  
    **Drake**, **Taylor Swift**, and **Bad Bunny** dominate global market presence, reinforcing their mainstream appeal across platforms (Spotify, YouTube, TikTok). To maximize festival success, a balanced lineup of globally recognized artists and viral sensations is essential to attract diverse audiences
    """)
    # 🔵 Diversity and Adaptability
    st.markdown("### Diversity and Adaptability")  
    df['artist_genres'] = df['artist_genres'].astype(str)

    df['artist_genres'] = df['artist_genres'].apply(lambda x: ast.literal_eval(x) if x.startswith("[") and x.endswith("]") else [])

    genre_counts_filtered = Counter([genre for genres in df['artist_genres'] for genre in genres])

    top_10_genres_filtered = genre_counts_filtered.most_common(10)
    top_10_genres_filtered_df = pd.DataFrame(top_10_genres_filtered, columns=["Genre", "Number of Artists"])

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.barh(top_10_genres_filtered_df["Genre"], top_10_genres_filtered_df["Number of Artists"])
    ax.set_xlabel("Number of Artists")
    ax.set_ylabel("Music Genres")
    ax.set_title("Top 10 Most Common Music Genres")
    ax.invert_yaxis()  
    st.pyplot(fig)
    
    st.markdown("""
    
    ### 🔍 **Key Insights:**  
    Reggaeton, pop, and rap dominate the music industry, aligned with the most influential artists like Bad Bunny, Drake, and Taylor Swift. Genres like Latin trap and urbano latino have a strong impact through TikTok, amplifying the importance of viral trends.
    """)            
# === Conclusion ===
with tab3:
    
    st.markdown("### 🎯 Conclusion")
    data = {
    "Category": [
        "Headliners",
        "Viral & Emerging Artists",
        "Musical & Geographical Diversity",
        "Digital Trends & Social Engagement"
    ],
    "Proposed Artists": [
        "Bad Bunny, Taylor Swift, Drake, The Weeknd",
        "Kevin MacLeod, The King Khan & BBQ Show, Jawsh 685, Conkarah ft. Shaggy, Tones and I",
        "BLACKPINK, Rema, Feid, Wizkid, Karol G",
        "BTS/Jungkook, Doja Cat, Lil Nas X, Ice Spice, Peso Pluma"
    ],
    "Why?": [
        "Leading streaming charts, ensuring massive attendance and global recognition.",
        "TikTok and YouTube stars attracting a young audience and driving strong digital engagement.",
        "Representing K-pop, Afrobeats, and Reggaeton, ensuring international reach and cultural diversity.",
        "Constantly trending on TikTok and YouTube, guaranteeing media coverage and online engagement."
    ]
}

    df = pd.DataFrame(data)
    st.markdown("##### 🎶 Artist Selection for the Festival (Version 0 - Preliminary)")
    #st.table(df)  
    # Suppression de l'index
    st.table(df.style.hide(axis="index"))
    
    st.markdown("### 🔮 Future Considerations")
    
    with st.expander("**Additional Considerations for a Refined Selection**"):
        st.markdown("""
        - 📱 **Social Media Influence**: Engagement levels on Instagram, Twitter, and fan interactions.  
        - 🎤 **Live Performance Appeal**: Tour history, ticket sales, and concert attendance impact.  
        - 💰 **Budget & Scheduling Constraints**: Artist fees and availability.  
        - 👥 **Target Audience & Age Groups**: Matching artists to the festival’s main demographic.  
        - 📅 **Time of Year & Seasonality**: Choosing artists based on festival timing and audience trends.
        - 🌍 **Cultural & Regional Relevance**: Ensuring artists resonate with the festival’s location and audience.
  
        """)

    st.info(
        "Rather than finalizing a fixed list of artists, this study serves as a foundation for deeper analysis. By integrating additional factors—such as social media influence, live performance appeal, budget constraints, and audience demographics—we can refine the selection process. This approach ensures a well-balanced, culturally relevant, and strategically curated festival lineup, maximizing audience engagement and overall success! "
    
    )

