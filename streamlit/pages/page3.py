import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import ast
from collections import Counter 

st.markdown(
    "<h1 style='text-align: center;'> Which selection of artists will ensure the success of a music festival?</h1>",
    unsafe_allow_html=True,
)

tabs = ["Introduction", "Analysis Factors", "Conclusion", "Tools & Data"]
selected_tab = st.radio("", tabs, horizontal=True)

if selected_tab == "Introduction":
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

    image_path = "/Users/medazz/code/streamlit_spotify_project_ghl/streamlit/images/image_festival.jpg" 
    st.image(image_path, use_column_width=True)

elif selected_tab == "Analysis Factors":
    st.markdown("## Popularity")  
    st.markdown("### 1- Top Spotify Artists") 

    file_path = "/Users/medazz/code/streamlit_spotify_project_ghl/data/cleaned_Spotify_Songs_2024.csv" 
    
    
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
  
    This graph displays the **Top 10 Most Listened Artists in the World**, based on streaming volume.  

    #### 🔍 **Key Insights:**  
    - **Most Popular Artists**: Bad Bunny, The Weeknd, Drake, and Taylor Swift lead in streaming volume.  
    - **Correlation Between Tracks and Popularity**: Artists with a higher number of tracks tend to have higher streaming volumes.  
    - **Significant Disparity**: The top four artists have a noticeable gap compared to the rest of the ranking.  
    - **Strategy for a Music Festival**: Booking these artists could maximize audience attendance and engagement.  
 
    """)
    st.markdown("### 2- Popular Artists")  
    st.markdown("""
    The Popularity Score is a composite metric that quantifies an artist's overall popularity by combining Spotify Popularity, Spotify Streams, YouTube Views, TikTok Views, and Shazam Counts, with each metric scaled appropriately. It provides a unified measure to compare artists across multiple platforms based on streaming and engagement data.
     """)
    # Calculation of popularity score by combining multiple sources (normalisation of scores to be able to do addition)
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
    ax.grid(axis='y', linestyle='--', alpha=0.7)

    st.pyplot(fig)
    st.markdown("""

    #### 🔍 **Key Insights:**  
    - **Different Rankings**: The most streamed artists are not necessarily the most popular across all platforms.
    - **Unexpected Leaders**: Kevin MacLeod and The King Khan & BBQ Show rank highest due to engagement beyond traditional streaming.
    - **Mainstream Artists Still Strong**: Bad Bunny, Taylor Swift, and Drake maintain high popularity across platforms. 
    - **Multi-Platform Impact**: Popularity is driven by more than just streams—YouTube, TikTok, and Shazam also play a key role.
 
    """)
    st.markdown("## Virality and Social Impact")  
    st.markdown("### 1- YouTube Views and Likes")  
  
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
    ax.grid(axis="x", linestyle="--", alpha=0.7)
    st.pyplot(fig)
    
    st.markdown("### 2- TikTok Posts, Likes et Views") 
     # Calculate TikTok Impact Score
    data_cleaned["TikTok Impact"] = (
        data_cleaned["TikTok Posts"].fillna(0) +
        data_cleaned["TikTok Likes"].fillna(0) / 1000 +
        data_cleaned["TikTok Views"].fillna(0) / 1e6
    )


    top_tiktok_tracks = data_cleaned.sort_values(by="TikTok Impact", ascending=False).head(10)

    top_tiktok_tracks = top_tiktok_tracks.drop_duplicates(subset=["Track", "Artist"])

    fig, ax = plt.subplots(figsize=(12, 6))
    ax.barh(
        top_tiktok_tracks["Track"] + " - " + top_tiktok_tracks["Artist"], 
        top_tiktok_tracks["TikTok Impact"]
    )
    ax.set_xlabel("TikTok Impact Score (Views in Millions + Likes in Thousands)")
    ax.set_ylabel("Track")
    ax.set_title("Top 10 Viral Songs on TikTok (2024)")
    ax.invert_yaxis()
    ax.grid(axis="x", linestyle="--", alpha=0.7)

    st.pyplot(fig)
    st.markdown("### 3- Shazam Counts ") 
    data_cleaned["Track_Artist"] = data_cleaned["Track"] + " - " + data_cleaned["Artist"]
    top_shazam = data_cleaned[["Track_Artist", "Shazam Counts"]].sort_values(by="Shazam Counts", ascending=False).head(10)
    st.set_option('deprecation.showPyplotGlobalUse', False)
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
    
    st.markdown("## Geographic Influence")
    file_path = "/Users/medazz/code/streamlit_spotify_project_ghl/data/Merged_Spotify_Data_with_region_spotyfolow_markets.csv"
    df = pd.read_csv(file_path)
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
    
    st.markdown("## Diversity et Adaptability")
    df['artist_genres'] = df['artist_genres'].astype(str)

    df['artist_genres'] = df['artist_genres'].apply(lambda x: x if x.startswith("[") and x.endswith("]") else "[]")

    df['artist_genres'] = df['artist_genres'].apply(lambda x: ast.literal_eval(x) if x != "[]" else [])


    df_non_empty_genres = df[df['artist_genres'].apply(lambda x: len(x) > 0)]

    genre_counts_filtered = Counter([genre for genres in df_non_empty_genres['artist_genres'] for genre in genres])

    top_10_genres_filtered = genre_counts_filtered.most_common(10)
    

    top_10_genres_filtered_df = pd.DataFrame(top_10_genres_filtered, columns=["Genre", "Number of Artists"])

    
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.barh(top_10_genres_filtered_df["Genre"], top_10_genres_filtered_df["Number of Artists"])
    ax.set_xlabel("Number of Artists")
    ax.set_ylabel("Music Genres")
    ax.set_title("Top 10 Most Common Music Genres")
    ax.invert_yaxis()  
    ax.grid(axis="x", linestyle="--", alpha=0.7)
    st.pyplot(fig)
    st.markdown("""
    
    ### 🔍 **Key Insights:**  
    Le **reggaeton**, la **pop** et le **rap** dominent l’industrie musicale, alignés avec les artistes les plus influents comme Bad Bunny, Drake et Taylor Swift. Les genres comme le trap latino et l’urbano latino bénéficient d’un fort impact via TikTok, renforçant l’importance des tendances virales.
    """)            
elif selected_tab == "Conclusion":

    st.markdown("## 🎯 Conclusion")

    st.info(
        "This analysis underscores that an artist's popularity is shaped by multiple elements, including **streaming metrics, geographic reach, and prevailing music trends**. "
        "However, this is merely a **preliminary assessment**, and additional considerations are necessary for an **optimal festival artist selection**."
    )

    st.markdown("### 🔍 Key Takeaways")
    st.markdown("""
    - **Popularity is multi-faceted**: Digital presence across platforms (Spotify, YouTube, TikTok, Shazam) plays a major role.  
    - **Geographic influence is key**: The most successful artists have a widespread market presence.  
    - **Genre preferences drive demand**: Reggaeton, pop, and rap continue to dominate global music charts.  
    """)

    with st.expander("**Additional Considerations for a Refined Selection**"):
        st.markdown("""
        - 📱 **Social Media Influence**: Engagement levels on Instagram, Twitter, and fan interactions.  
        - 🎤 **Live Performance Appeal**: Tour history, ticket sales, and concert attendance impact.  
        - 💰 **Budget & Scheduling Constraints**: Artist fees and availability.  
        - 👥 **Target Audience & Age Groups**: Matching artists to the festival’s main demographic. 
        - 📅 **Time of Year & Seasonality**: Choosing artists based on festival timing and audience trends.  
        """)

    st.info(
        "Rather than settling on a **fixed list of artists**, this study provides a **foundation for further analysis**. "
        "By incorporating **additional factors**, we can curate a **more relevant and strategic festival lineup**, ensuring maximum audience engagement and success! 🎶"
    )

elif selected_tab == "Tools & Data":
    st.markdown("## Tools & Data")
    
    st.markdown("### Data")
    st.markdown("[🔗 Lien vers Kaggle](https://www.kaggle.com/datasets/nelgiriyewithana/most-streamed-spotify-songs-2024)")
    
    st.markdown("### Tools")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.image("https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg", width=80)
        st.markdown("**Python**")
    
    with col2:
        st.image("https://streamlit.io/images/brand/streamlit-mark-color.png", width=80)
        st.markdown("**Streamlit**")
    
    with col3:
        st.image("https://seaborn.pydata.org/_images/logo-mark-lightbg.svg", width=80)
        st.markdown("**Seaborn**")
    
    col4, col5, col6 = st.columns(3)
    
    with col4:
        st.image("https://upload.wikimedia.org/wikipedia/commons/8/84/Matplotlib_icon.svg", width=80)
        st.markdown("**Matplotlib**")
    
    with col5:
        st.image("/Users/medazz/code/streamlit_spotify_project_ghl/streamlit/images/pandas.png", width=80)
        st.markdown("**Pandas**")
        
    with col6:
        st.image("/Users/medazz/code/streamlit_spotify_project_ghl/streamlit/images/apify.png", width=80)
        st.markdown("**Apify**")
