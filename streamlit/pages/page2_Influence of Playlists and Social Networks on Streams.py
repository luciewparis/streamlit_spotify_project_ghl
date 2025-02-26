import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import seaborn as sns
import plotly.io as pio
pio.templates.default = 'plotly' 

st.markdown("<h1 style='text-align: center;'> Analysis of the Impact of Music Platforms and Social Networks on Spotify Streams</h1>",
unsafe_allow_html=True,)

tabs = st.tabs(["       Spotify     ", "    Other platforms     ", "    YouTube     ", "    TikTok      "])

#tabs = ["Spotiy", "Other platforms", "YouTube", "TikTok"]
#selected_tab = st.radio("", tabs, horizontal=True)

data=pd.read_csv('./data/2024_most_streamed_clean_final_1.csv')





with tabs[0]:
    st.header("Spotify")
    st.subheader('Trends and Influences in Spotify Streams: Analyzing Yearly Data and Popularity Factors')
    st.image('https://www.ecranmobile.fr/photo/art/grande/78329478-56858046.jpg?v=1707777032', width=200)
    
    st.write("")
    st.write("")
    st.write("Playlists and social networks are often considered to influence streams on Spotify. This section seeks to examine their potential role in the visibility and popularity of songs, to determine whether there is a link.")
    
    st.write("")
    st.write("")
    
    st.markdown('<h3 style="font-size: 20px;">Years with the Most Top Streamed Songs on Spotify</h3>', unsafe_allow_html=True)

    #st.write('The most streamed titles are mainly from the last 8 years, which could be linked to the growing influence of social networks during this period. It would be worth investigating whether this link holds true.')
    
    #convert the column in the good format 
    data["Release Date"] = pd.to_datetime(data["Release Date"], errors='coerce')

    # transform the date to keep the year 
    data["Year"] = data["Release Date"].dt.year.astype(int)

    #Group the data by "Year" and count the number of occurrences for each year. 
    song_count_by_year = data.groupby("Year").count()[["Track"]]

    
    import plotly.figure_factory as ff

    fig = px.bar(song_count_by_year,
                 y="Track",
                 range_x=(2000,2020)
             )
    fig.update_layout(template='plotly')
    st.plotly_chart(fig)  
    
      
    st.markdown("""
    #### 🔍 **Key Insights:**  
    - The most streamed titles are mainly from the last 3 to 5 years""")
    
    st.write("")
    st.write("")
    
    st.markdown('<h3 style="font-size: 20px;">Distribution of Spotify Streams</h3>', unsafe_allow_html=True)


    fig = px.histogram(
        data, x="Spotify Streams", 
        labels={"Spotify Streams": "Streams Spotify", "count": "Streams Spotify"})
    st.plotly_chart(fig)
    
    st.markdown("""
   #### 🔍 **Key Insights:**  
    - he majority of tracks in this ranking have fewer than 300 million streams
    - Only 12% of the tracks have reached a billion streams, """)
    
    st.write("")
    st.write("")

    st.markdown('<h3 style="font-size: 20px;">Popularity Score vs. Streams: A Weak Correlation</h3>', unsafe_allow_html=True)

   
    # Keep values other than 0 
    filtered_data = data[data["Spotify Popularity"] != 0]
    fig = px.scatter(filtered_data, x="Spotify Popularity", y="Spotify Streams")
    st.plotly_chart(fig)
    
    
    st.markdown("""
    #### 🔍 **Key Insights:**  
    - Weak correlation observed between popularity score and the number of streams
    - Other contributing factors to popularity likely include:
        - Recent listening trends.
        - Track visibility in highly popular playlists.
    """)
    
    
    st.write("")
    st.write("")
    st.write("")
    
    st.markdown('<h3 style="font-size: 20px;">Impact of Playlists on Streaming Numbers</h3>', unsafe_allow_html=True)
    
   
    # Keep values other than 0 
    filtered_data = data[data["Spotify Playlist Count"] != 0]

    fig = px.scatter(
    filtered_data,
    x="Spotify Playlist Count", 
    y="Spotify Streams",
    trendline="ols" 
    )

    st.plotly_chart(fig,use_container_width=False)
    
    
    st.markdown("""
    #### 🔍 **Key Insights:**  
    - Correlation observed between the number of streams and playlist additions.
    - The more a song is added to playlists, the higher its chances of being streamed.     
    """)
    

    #st.write('After analyzing the Spotify popularity score, the number of streams was examined in relation to the streams themselves. The goal was to determine the correlation between the two. A correlation was observed, which seems logical, as the more a song is added to a playlist, the higher its chances of being streamed.')



with tabs[1]:
    st.header("Other Music Platforms")
    st.subheader('Exploring the correlation of Other Platforms on Spotify Streams: Apple Music and Deezer')
    st.image('https://www.apple.com/newsroom/images/product/apple-music/apple_music-update_hero_08242021_inline.jpg.large_2x.jpg', width=200)
    st.image('https://www.varactu.fr/wp-content/uploads/2023/11/LOGO-DEEZER-2023.jpg', width=160)
    
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    
    st.markdown('<h3 style="font-size: 20px;">Limited Correlation Between Other Platforms and Spotify Streams</h3>', unsafe_allow_html=True)




    # Keep values other than 0 and keep the values above 500
    filtered_data = data[(data["Apple Music Playlist Count"] != 0) & (data["Apple Music Playlist Count"] <= 500)]

    fig = px.scatter(
    filtered_data,
    x="Apple Music Playlist Count",
    y="Spotify Streams",
    title="Spotify Streams and Apple Music Playlists",
    trendline="ols" 
    )

    st.plotly_chart(fig)
   


    # Keep values other than 0 and keep the values above 500
    filtered_data = data[(data["Deezer Playlist Count"] != 0) & (data["Deezer Playlist Count"] <= 400)]

    fig = px.scatter(
    filtered_data,
    x="Deezer Playlist Count",
    y="Spotify Streams",
    title="Spotify Streams and Deezer Playlists",
    trendline="ols" 
)

    st.plotly_chart(fig)
    
    st.markdown("""
    #### 🔍 **Key Insights:**  
    - Popular songs vary from platform to platform.
    - Each platform values songs according to its own criteria and audience.   
    """)



with tabs[2]:
    st.header('YouTube')
    st.subheader('YouTube vs Spotify: Investigating the Correlation between Views, Likes, and Streams')
    st.image('https://upload.wikimedia.org/wikipedia/commons/e/ef/Youtube_logo.png', width=180)
    
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    
    st.write('After analyzing the popularity score and competing platforms (especially playlists), it\'s relevant to look at possible links with YouTube, as many songs are listened to on this platform.”')

    st.write("")
    st.write("")
    
    st.markdown('<h3 style="font-size: 20px;">Discrepancy Between YouTube Interaction and Spotify Streams</h3>', unsafe_allow_html=True)
    
    
    
    
    # Keep values other than 0 and keep values below 5000000000
    filtered_data_ytb_views = data[(data["YouTube Views"] != 0) & (data["YouTube Views"] <= 5000000000)]

    fig = px.scatter(filtered_data_ytb_views,
                 x="YouTube Views", 
                 y="Spotify Streams",
                 trendline="ols", 
                 title="Exploring the Link Between Spotify streams and YouTube views")
    st.plotly_chart(fig)

    # Keep values other than 0 and keep values below 50000000
    filtered_data_ytb_likes = data[(data["YouTube Likes"] != 0) & (data["YouTube Likes"] <= 50000000)]

    fig = px.scatter(filtered_data_ytb_likes,
                 x="YouTube Likes", 
                 y="Spotify Streams",
                 trendline="ols", 
                 title="Exploring the Link Between Spotify streams and YouTube likes")
    st.plotly_chart(fig)
    
    
   
     
    st.write("")
    st.write("")
    
    st.markdown('<h3 style="font-size: 20px;">Comparing the Top 10 Tracks on Spotify and YouTube"</h3>', unsafe_allow_html=True)
    
    
    #Sort the dataset in descending order based on the "Spotify Streams" column and select the top 10 most streamed songs.  
    most_popular_spotify = data.sort_values(by='Spotify Streams', ascending=False).head(10)


    fig = px.bar(most_popular_spotify, x="Track", 
    y="Spotify Streams", 
    title="TOP 10 most popular songs on Spotify")   
    st.plotly_chart(fig)
    
    
    #Sort the dataset in descending order based on the "YouTube Views" column and select the top 10 most viewed songs.  
    most_popular_youtube = data.sort_values(by='YouTube Views', ascending=False).head(10)
    #print(most_popular_youtube[['Track', 'YouTube Views']])
    fig = px.bar(most_popular_youtube, x="Track", 
    y="YouTube Views", 
    title="TOP 10 most popular songs on YouTube")
    st.plotly_chart(fig)
    
    st.markdown("""
    #### 🔍 **Key Insights:**  
    - No correlation between views/likes on YouTube and streams on Spotify.
    - YouTube focuses on the visual experience, while Spotify is audio-centered.
    - Audiences may differ, with distinct preferences on each platform.
    """)
    
    
with tabs[3]:
    st.header("Tiktok")
    st.subheader('TikTok\'s Viral Power: Analyzing the Influence of Posts and Likes on Spotify Streams')
    st.image('https://c0.lestechnophiles.com/www.numerama.com/wp-content/uploads/2018/11/tik-tok.jpg?resize=1200,675&key=afd29a7b&watermark', width=200)
    
    
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    
    st.write("After YouTube, we turn to TikTok, the most viral social network that generates much of the trends. As with the other platforms, the goal is to analyze whether there is a correlation.")
     
    st.write("")
    st.write("")
    
    st.markdown('<h3 style="font-size: 20px;">Common Trends in Popular Genres Across Spotify and TikTok</h3>', unsafe_allow_html=True)
    
    
    
    # Loading the new csv file with top songs Spotify 
    df_genre_spotify = pd.read_csv('./data/top 100 spotify  - top_100_songs_spotify (2).csv')
    
    # Group the dataset by the first genre ("artist_genres1")  and sum the total "Spotify Streams" for each genre. 
    top_5_genres_spotify = df_genre_spotify.groupby('artist_genres1')['Spotify Streams'].sum().reset_index()


    # Sort the genres by total "Spotify Streams" in descending order  and select the top 5 genres with the highest number of streams. 
    top_5_genres_spotify = top_5_genres_spotify.sort_values(by="Spotify Streams", ascending=False).head(5)

    fig = px.bar(top_5_genres_spotify, x="artist_genres1", 
    y="Spotify Streams", 
    title= "Most popular genre on Spotify (top 100)",
    labels={"artist_genres1": "Musical Genre"},
    category_orders={"Spotify Streams": top_5_genres_spotify["Spotify Streams"].tolist()})
    st.plotly_chart(fig)
     

    # Loading the new csv file with top songs TikTok
    df_genre_tiktok =pd.read_csv('./data/top_100_songs_tiktok - top_100_songs_tiktok.csv')


    # Group the dataset by the first genre ("artist_genres1")  and sum the total "TikTok Views" for each genre. 
    top_5_genres_tiktok = df_genre_tiktok.groupby('artist_genres')['TikTok Views'].sum().reset_index()
    
    # Sort the genres by total "TikTok Views" in descending order  and select the top 5 genres with the highest number of streams. 
    top_5_genres_tiktok = top_5_genres_tiktok.sort_values(by='TikTok Views', ascending=False).head(5)
   

    fig = px.bar(top_5_genres_tiktok, x="artist_genres", 
    y="TikTok Views", 
    title= "Most popular genre on TikTok views (top 100)",
    labels={"artist_genres": "Musical Genre"}, 
    category_orders={"TikTok Views": top_5_genres_tiktok["TikTok Views"].tolist()})
    
    st.plotly_chart(fig)
       

    
    #Keep values other than 0 and keep values below 50000000
    filtered_data_tiktok_views = data[(data["TikTok Views"] != 0) & (data["TikTok Views"] <= 50000000)]
    fig_tiktok_streams = px.scatter(filtered_data_tiktok_views, 
    x="TikTok Views", 
    y="Spotify Streams", 
    trendline="ols", 
    title="Exploring the Link Between Spotify streams and TikTok views")
    st.plotly_chart(fig_tiktok_streams)
    
    st.markdown("""
    #### 🔍 **Key Insights:**  
    - The top genres on Spotify and TikTok shows similar trends (ex: pop and reggaeton )
    - No correlation between TikTok posts/likes and Spotify streams.
    - Hypothesis: Likes and views are more related to the content of the post than the song used.
    """)

    
    