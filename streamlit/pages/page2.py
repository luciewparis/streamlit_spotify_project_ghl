import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

tabs = st.tabs(["Features SPOTIFY", "Other platforms", "YOUTUBE", "TikTok", "Genre"])

df=pd.read_csv('/Users/betsy/Documents/streamlit_spotify_project_ghl/data/2024_most_streamed_clean_final_1.csv')
data=df


st.title("Analysis of the Impact of Platforms and Social Networks on Spotify Streams")



with tabs[0]:
    st.header("Features SPOTIFY")
    st.write('The most streamed titles are mainly from the last 3 to 5 years, which could be linked to the growing influence of social networks during this period. It would be worth investigating whether this link holds true.')
    yearly_streams = data.groupby("Release Date")["Spotify Streams"].sum().reset_index()


    fig = px.bar(yearly_streams, x="Release Date", 
    y="Spotify Streams", 
    title="Histogram of Spotify Streams by Year of Release"
    )
    st.plotly_chart(fig)

    st.write('The distribution histogram shows that the majority of tracks in this ranking have fewer than 300 million streams. Only 12% of the tracks have reached a billion streams, highlighting a concentration of streams around the lower values, with a small percentage of tracks achieving exceptional numbers. ')

    fig = px.histogram(data, x="Spotify Streams", title="Spotify Streams's distribution")
    st.plotly_chart(fig)

    st.title("")

    st.write('The aim of this analysis was to identify any correlation between the popularity score and the total number of streams of a track. The results show that the correlation is relatively weak, suggesting that other factors influence the calculation of the popularity score. These include the dynamics of recent listens and the track\'s presence in playlists, particularly those with high visibility.')


    filtered_data = data[data["Spotify Popularity"] != 0]
    fig = px.scatter(filtered_data, x="Spotify Popularity", y="Spotify Streams", title="Exploring the Link Between Spotify streams and Popularity")
    st.plotly_chart(fig)

    st.write('After analyzing the Spotify popularity score, the number of streams was examined in relation to the streams themselves. The goal was to determine the correlation between the two. A correlation was observed, which seems logical, as the more a song is added to a playlist, the higher its chances of being streamed.')


    filtered_data = data[data["Spotify Playlist Count"] != 0]

    fig = px.scatter(
    filtered_data,
    x="Spotify Playlist Count", 
    y="Spotify Streams",
    title="Exploring the Link Between Spotify Streams and Spotify Playlist Count",
    trendline="ols" 
    )

    st.plotly_chart(fig)





with tabs[1]:
    st.header("Other plateforms")
    st.write("Voici les détails pour l'onglet 2.")
    st.title('Other plateforms ')
    st.write('To confirm this correlation, a test was conducted on the playlist count of a platform like Apple Music.')

    st.write('Once again, the correlation is confirmed: playlists show a significant relationship with the number of streams. Many playlists are public, and when a playlist is played, a song can be streamed without the initial intention of playing that specific track.')

    filtered_data = data[(data["Apple Music Playlist Count"] != 0) & (data["Apple Music Playlist Count"] <= 500)]

    fig = px.scatter(
    filtered_data,
    x="Apple Music Playlist Count",
    y="Spotify Streams",
    title="Exploring the Link Between Spotify Streams and Apple Music Playlist Count",
    trendline="ols" 
    )

    st.plotly_chart(fig)

    filtered_data = data[(data["Deezer Playlist Count"] != 0) & (data["Deezer Playlist Count"] <= 400)]

    fig = px.scatter(
    filtered_data,
    x="Deezer Playlist Count",
    y="Spotify Streams",
    title="Exploring the Link Between Spotify Streams and Deezer Playlist Count",
    trendline="ols" 
)

    st.plotly_chart(fig)




with tabs[2]:
    st.header("YOUTUBE")
    st.write("Voici les détails pour l'onglet 3.")
    
    st.title('YOUTUBE')

    st.write('Analyzing the popularity score and competing platforms (playlists) highlights the relevance of examining possible links with YouTube, as many songs are listened to on this platform.')

    st.write('Correlation youtube views and spotify streams')
    st.write('A comparison between views and likes on YouTube and streams on Spotify revealed no correlation. This may be explained by differences in usage: YouTube focuses on the visual experience, while Spotify concentrates on listening to music. What\'s more, the audiences for the two platforms may be distinct, and tracks that are popular on one are not necessarily popular on the other, reflecting different preferences')

    filtered_data_ytb_views = data[(data["YouTube Views"] != 0) & (data["YouTube Views"] <= 5000000000)]

    fig = px.scatter(filtered_data_ytb_views,
                 x="YouTube Views", 
                 y="Spotify Streams",
                 trendline="ols", 
                 title="Exploring the Link Between Spotify streams and YouTube views")
    st.plotly_chart(fig)

    filtered_data_ytb_likes = data[(data["YouTube Likes"] != 0) & (data["YouTube Likes"] <= 50000000)]

    fig = px.scatter(filtered_data_ytb_likes,
                 x="YouTube Likes", 
                 y="Spotify Streams",
                 trendline="ols", 
                 title="Exploring the Link Between Spotify streams and YouTube likes")
    st.plotly_chart(fig)




with tabs[3]:
    st.header("Tiktok")
    
    st.write("After YouTube, we turn to TikTok, the most viral social network that generates much of the trends. As with the other platforms, the goal is to analyze whether there is a correlation.")
    
    st.write('There is no correlation between TikTok posts and likes and Spotify streams. One possible hypothesis is that the likes and views are more related to the content of the post itself rather than the song used.')
    
    filtered_data_ytb_likes = data[(data["TikTok Views"] != 0) & (data["TikTok Views"] <= 50000000)]
    fig_tiktok_streams = px.scatter(
    data, 
    x="TikTok Views", 
    y="Spotify Streams", 
    trendline="ols", 
    title="Exploring the Link Between Spotify streams and TikTok views")
    st.plotly_chart(fig)

    tiktok_streams =data.sort_values(by='Spotify Streams', ascending=False).head(100)
    likes_streams = px.scatter(
    tiktok_streams, 
    x="TikTok Posts", 
    y="TikTok Likes", 
    size="Spotify Streams", 
     
    title="How TikTok Likes and Posts Influence Spotify Streams"
    )
    fig.update_xaxes(range=[1, 1]) 

    fig.update_yaxes(range=[1, 1])  

    st.plotly_chart(likes_streams)

    
with tabs[4]:
    df_genre_spotify = pd.read_csv('/Users/betsy/Documents/streamlit_spotify_project_ghl/data/top 100 spotify  - top_100_songs_spotify (2).csv')
    data=df_genre_spotify
    
    st.header("Genre")
    
    
    top_5_genres_spotify = data.groupby('artist_genres1')['Spotify Streams'].sum().reset_index()

    top_5_genres_spotify = top_5_genres_spotify.sort_values(by="Spotify Streams", ascending=False).head(5)

    fig = px.bar(top_5_genres_spotify, x="artist_genres1", 
    y="Spotify Streams", 
    title= "Most popular genre on Spotify (top 100)",
    labels={"artist_genres1": "Genre musical"},
    category_orders={"Spotify Streams": top_5_genres_spotify["Spotify Streams"].tolist()})
    st.plotly_chart(fig)
     


    df_genre_tiktok =pd.read_csv('/Users/betsy/Documents/streamlit_spotify_project_ghl/data/top_100_songs_tiktok - top_100_songs_tiktok.csv')

    top_5_genres_tiktok = df_genre_tiktok.groupby('artist_genres')['TikTok Views'].sum().reset_index()
    top_5_genres_tiktok = top_5_genres_tiktok.sort_values(by='TikTok Views', ascending=False).head(())
   

    fig = px.bar(top_5_genres_tiktok, x="artist_genres", 
    y="TikTok Views", 
    title= "Most popular genre on TikTok views (top 100)",
    labels={"artist_genres": "Genre musical"}, 
    category_orders={"TikTok Views": top_5_genres_tiktok["TikTok Views"].tolist()})
    
    st.plotly_chart(fig)
   