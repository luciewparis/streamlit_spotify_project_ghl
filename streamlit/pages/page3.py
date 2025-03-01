import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
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
    st.markdown("## 🚪 Introduction")
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
    st.markdown("## 📊 Analysis Factors")
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
    
    # Plotly bar chart
    fig = px.bar(
        top_artists, x="Artist", y="Spotify Streams", color="Number of Tracks",
        color_continuous_scale="Blues", title="TOP 10 Most Listened Artists in the World"
    )
    st.plotly_chart(fig)
    
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
   # Calculation of popularity score
    data_cleaned["Popularity Score"] = (
        data_cleaned["Spotify Popularity"].fillna(0) + 
        data_cleaned["Spotify Streams"].fillna(0) / 1e6 + 
        data_cleaned["YouTube Views"].fillna(0) / 1e6 +
        data_cleaned["TikTok Views"].fillna(0) / 1e6 + 
        data_cleaned["Shazam Counts"].fillna(0) / 1e5   
    )

    top_artists = data_cleaned.groupby("Artist")["Popularity Score"].sum().sort_values(ascending=False).head(10).reset_index()

    fig = px.bar(top_artists, x="Artist", y="Popularity Score", title="Top 10 Most Popular Artists (2024)")
    st.plotly_chart(fig)
    st.markdown("""

    #### 🔍 **Key Insights:**  
    - **Different Rankings**: The most streamed artists are not necessarily the most popular across all platforms.
    - **Unexpected Leaders**: Kevin MacLeod and The King Khan & BBQ Show rank highest due to engagement beyond traditional streaming.
    - **Mainstream Artists Still Strong**: Bad Bunny, Taylor Swift, and Drake maintain high popularity across platforms. 
    - **Multi-Platform Impact**: Popularity is driven by more than just streams—YouTube, TikTok, and Shazam also play a key role.
 
    """)
    st.markdown("### Virality and Social Impact")  
    st.markdown("#### 1- YouTube Views and Likes")  

    # YouTube Impact
    data_cleaned["YouTube Impact"] = (
        data_cleaned["YouTube Views"].fillna(0) / 1e6 +  
        data_cleaned["YouTube Likes"].fillna(0) / 1000
    )

    top_youtube_tracks = data_cleaned.nlargest(10, "YouTube Impact")
    fig = px.bar(top_youtube_tracks, x="Track", y="YouTube Impact", title="Top 10 Most Popular Songs on YouTube")
    st.plotly_chart(fig)
    
    st.markdown("#### 2- TikTok Posts, Likes et Views") 
    # TikTok Impact
    data_cleaned["TikTok Impact"] = (
        data_cleaned["TikTok Posts"].fillna(0) +
        data_cleaned["TikTok Likes"].fillna(0) / 1000 +
        data_cleaned["TikTok Views"].fillna(0) / 1e6
    )
    
    top_tiktok_tracks = data_cleaned.nlargest(10, "TikTok Impact")
    fig = px.bar(top_tiktok_tracks, x="Track", y="TikTok Impact", title="Top 10 Viral Songs on TikTok (2024)")
    st.plotly_chart(fig)
    
    st.markdown("#### 3- Shazam Counts") 
    # Shazam Counts
    top_shazam = data_cleaned.nlargest(10, "Shazam Counts")
    fig = px.bar(top_shazam, x="Track", y="Shazam Counts", title="Top 10 Songs by Shazam Search Count")
    st.plotly_chart(fig)
    
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
    try:
        df = pd.read_csv(file_path, encoding="latin1")
    except FileNotFoundError:
        st.error("Le fichier CSV des marchés n'a pas été trouvé. Vérifiez le chemin d'accès.")
        st.stop()

# Fonction de validation et conversion
    def safe_literal_eval(value):
        try:
            return ast.literal_eval(value) if isinstance(value, str) and value.startswith("[") and value.endswith("]") else []
        except (SyntaxError, ValueError):
            return []

    df["track_markets_cleaned"] = df["track_markets"].apply(lambda x: len(safe_literal_eval(x)))

    artist_total_markets = df.groupby("Artist")["track_markets_cleaned"].sum().nlargest(10).reset_index()

    fig = px.bar(artist_total_markets, x="Artist", y="track_markets_cleaned", title="Top 10 Artists by Total Market Presence")
    st.plotly_chart(fig)


    st.markdown("""

    #### 🔍 **Key Insights:**  
    **Drake**, **Taylor Swift**, and **Bad Bunny** dominate global market presence, reinforcing their mainstream appeal across platforms (Spotify, YouTube, TikTok). To maximize festival success, a balanced lineup of globally recognized artists and viral sensations is essential to attract diverse audiences
    """)
    # 🔵 Diversity and Adaptability
    st.markdown("### Diversity and Adaptability")  
    df['artist_genres'] = df['artist_genres'].astype(str)
    df['artist_genres'] = df['artist_genres'].apply(lambda x: ast.literal_eval(x) if x.startswith("[") and x.endswith("]") else [])
    genre_counts_filtered = Counter([genre for genres in df['artist_genres'] for genre in genres])
    top_10_genres_filtered_df = pd.DataFrame(genre_counts_filtered.most_common(10), columns=["Genre", "Number of Artists"])
    
    fig = px.bar(top_10_genres_filtered_df, x="Genre", y="Number of Artists", title="Top 10 Most Common Music Genres")
    st.plotly_chart(fig)
    
    st.markdown("""
    
    ### 🔍 **Key Insights:**  
    Reggaeton, pop, and rap dominate the music industry, aligned with the most influential artists like Bad Bunny, Drake, and Taylor Swift. Genres like Latin trap and urbano latino have a strong impact through TikTok, amplifying the importance of viral trends.
    """)   
             
# === Conclusion ===
with tab3:
    
    st.markdown("### 🎯 Conclusion")
    artists = {
        "Headliners": [
        {"name": "Bad Bunny", "image": "./streamlit/images/bad bunny.jpg"},
        {"name": "Taylor Swift", "image": "./streamlit/images/taylor swift.jpg"},
        {"name": "Drake", "image": "./streamlit/images/rake.jpeg"},
        {"name": "The Weeknd", "image": "./streamlit/images/the weekend.jpg"}
        ],
    "Viral & Emerging Artists": [
        {"name": "Shaggy", "image": "./streamlit/images/Shaggy.jpg"},
        {"name": "Tones and I", "image": "./streamlit/images/Tones and I.jpg"},
        {"name": "Jawsh 685", "image": "./streamlit/images/jawch.jpg"},
        {"name": "Conkarah", "image": "./streamlit/images/chokrah.jpeg"}
    ],
    "Musical & Geographical Diversity": [
        {"name": "BLACKPINK", "image": "./streamlit/images/blackpink.jpg"},
        {"name": "Rema", "image": "./streamlit/images/rema.jpeg"},
        {"name": "Feid", "image": "./streamlit/images/feid.jpg"},
        {"name": "Wizkid", "image": "./streamlit/images/wizkid.jpeg"}
    ],
    "Digital Trends & Social Engagement": [
        {"name": "BTS/Jungkook", "image": "./streamlit/images/BTS:Jungkook.jpg"},
        {"name": "Doja Cat", "image": "./streamlit/images/doja.jpg"},
        {"name": "Lil Nas X", "image": "./streamlit/images/lilnas.jpg"},
        {"name": "Ice Spice", "image": "./streamlit/images/Ice Spice .jpg"}
    ]
}

    st.markdown("The majority of **Spotify users** are young adults aged 18 to 34, with a strong presence in the United States. With this in mind, we have curated a festival lineup based on our dataset, tailored to their musical preferences and current trends.")
    st.markdown("##### 🎶 Artist Selection for the Festival (Version 0 - Preliminary)")

# Affichage des artistes par catégorie
    for category, artist_list in artists.items():
        st.subheader(category)
        cols = st.columns(4)  
        for i, artist in enumerate(artist_list):
            with cols[i % 4]:  
                st.image(artist["image"], width=150)
                st.write(f"**{artist['name']}**")
   
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


