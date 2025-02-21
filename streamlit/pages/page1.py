import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from streamlit_player import st_player

tab1, tab2, tab3 = st.tabs(["     Definitions     ", "     Profile overview     ", "     Details     "])

################# TAB 1 #################
with tab1:
    st.title("Definitions of the audio features used for our analysis")


    st.header("Danceability")
    st.markdown("Danceability describes how suitable a track is for dancing based on a combination of musical elements including tempo, rhythm stability, beat strength, and overall regularity. A value of 0.0 is least danceable and 100% is most danceable.")
    st.markdown("Example of a track with **high danceability (96%)**: #511")
    st_player("https://youtu.be/pekzpzNCNDQ?si=WpQ-nqNY1GBOdtZA&t=68")
    st.markdown("Example of a track with *low danceability (23%)*: #372")

    st.markdown("Example of a track with **high Speechiness (64%)**: #856 ")
    st_player("https://youtu.be/OZgQnRcGZXs?si=2znKGsUTzCvjPXUt&t=63")
    st.markdown("Example of a track with *low Speechiness (2%)*: this track at position #61 has half the amount of lyrics of the above track")
    st_player("https://youtu.be/RB-RcX5DS5A?si=EzygWpobFxjUylIt")

    st.header("Valence")
    st.markdown("A measure from 0.0 to 100% describing the musical positiveness conveyed by a track. Tracks with high valence sound more positive (e.g. happy, cheerful, euphoric), while tracks with low valence sound more negative (e.g. sad, depressed, angry).")
    st.markdown("Example of a track with **high Valence (97%)**: #50")
    st_player("https://youtu.be/dT2owtxkU8k?si=uEEVtwgJMZaReGcl&t=61")
    st.markdown("Example of a track with *low Valence (4%)*: #248")
    st_player("https://youtu.be/sVx1mJDeUjY?si=95YACnVJdXILYP3E&t=46")

    st.header("Energy")
    st.markdown("Energy is a measure from 0 to 100 and represents a perceptual measure of intensity and activity. Typically, energetic tracks feel fast, loud, and noisy. For example, death metal has high energy, while a Bach prelude scores low on the scale. Perceptual features contributing to this attribute include dynamic range, perceived loudness, timbre, onset rate, and general entropy.")
    st.markdown("Example of a track with **high Energy (97%)**: #337")
    st_player("https://youtu.be/w-sQRS-Lc9k?si=mSzmTEIok50eIBSE&t=16")
    st.markdown("Example of a track with *low Energy (9%)*: #941")
    st_player("https://youtu.be/cW8VLC9nnTo?si=KvrQU423ch8OrYJF&t=8")

    st.header("Acousticness")
    st.markdown("A confidence measure from 0 to 100 of whether the track is acoustic. 100% represents high confidence the track is acoustic.")
    st.markdown("Example of a track with **high Acousticness (97%)**: #83")
    st_player("https://youtu.be/KtlgYxa6BMU?si=mmUDpp8ZXBn-FGn-&t=27")
    st.markdown("Example of a track with *low Acousticness (0%)*: #34")
    st_player("https://youtu.be/tvTRZJ-4EyI?si=X2YEiJXjHDZxM2gU&t=7")

    st.header("Liveness")
    st.markdown("Detects the presence of an audience in the recording. Higher liveness values represent an increased probability that the track was performed live. A value above 80% provides strong likelihood that the track is live.")
    # st.markdown("Comparing tracks with different levels of instrumentalness and seeing the low impact of this feature on a track's success, we will not consider this audio feature as we do not find it insightful for our analysis.")
    st.markdown("Example of a track with **high Liveness (97%)**: #506")
    st_player("https://youtu.be/r2ma8WPRppk?si=ZcG8nV_wlHvk5qFD&t=3")
    st.markdown("Example of a track with *low Liveness (3%)*: #579")
    st_player("https://youtu.be/8dJyRm2jJ-U?si=p3cIwh0yYFtv1yKL&t=58") 

    st.header("Instrumentalness - not considered?")
    st.markdown("Predicts whether a track contains no vocals. 'Ooh' and 'aah' sounds are treated as instrumental in this context. Rap or spoken word tracks are clearly 'vocal'. The closer the instrumentalness value is to 100%, the greater likelihood the track contains no vocal content. Values above 50% are intended to represent instrumental tracks, but confidence is higher as the value approaches 100%.")
    # st.markdown("Comparing tracks with different levels of instrumentalness and seeing the low impact of this feature on a track's success, we will not consider this audio feature as we do not find it insightful for our analysis.")
    st.markdown("Example of a track with **high Instrumentalness (91%)**: #392")
    st_player("https://youtu.be/V8fYAAh5uuA?si=Bc-j6F34cU6bpmC2&t=36")
    st.markdown("Example of a track with *low Instrumentalness (0%)*: #1")
    st_player("https://youtu.be/4NRXx6U8ABQ?si=Id0ZtDRkjwR-Ue3h&t=73")

    st.header("BPM - not considered?")
    st.markdown("The overall estimated tempo of a track in beats per minute (BPM). In musical terminology, tempo is the speed or pace of a given piece and derives directly from the average beat duration.")
    st.markdown("Example of a track with **high BPM (180)**: not in the top tracks but for reference only")
    st_player("https://youtu.be/wiBXrkka-YA?si=4N6fKFnGL2SPRp1o&t=94")
    st.markdown("Example of a track with *low BPM (65)*: #781")
    st_player("https://youtu.be/npu0F7n4M9Y?si=iVMLN7uPJTGKVkuR&t=12")

# ################# TAB 2 #################
with tab2:
    st.title("What are the audio features of successful tracks in 2023?")

   # Get initial data
    df = pd.read_csv('./data/2023_Most_Streamed_clean_api_genre.csv')

    st.header("Comparison between TOP N")
    df_polar_2 = pd.DataFrame({
        'audio_feature': ['speechiness_%', 'danceability_%', 'valence_%', 'energy_%', 'acousticness_%', 'liveness_%', 'instrumentalness_%'],
        'metric': ['mean', 'mean','mean','mean','mean','mean','mean' ]
        })
    df_polar_2 = pd.concat([df_polar_2, df_polar_2, df_polar_2], ignore_index=True)
    df_top = df.iloc[:2]
    df_polar_2.loc[df_polar_2.index.isin(range(7,14)),'metric'] = 'max'
    df_polar_2.loc[df_polar_2.index.isin(range(14,21)),'metric'] = 'min'
    df_polar_2 = pd.DataFrame({
        'audio_feature': ['speechiness_%', 'danceability_%', 'valence_%', 'energy_%', 'acousticness_%', 'liveness_%', 'instrumentalness_%'],
        'metric': ['mean', 'mean','mean','mean','mean','mean','mean' ]
    })
    def get_metric(row):
        if row['metric'] == 'mean':
            return df_top[f"{row['audio_feature']}"].mean()
        elif row['metric'] == 'max':
            return df_top[f"{row['audio_feature']}"].max()
        elif row['metric'] == 'min':
            return df_top[f"{row['audio_feature']}"].min()
        else:
            return "metric not found"
    
    df_polar_2['value'] = df_polar_2.apply(get_metric, axis =1)

    # define top10
    df_polar_10 = df_polar_2.copy()
    df_top = df.iloc[:10]
    df_polar_10['value'] = df_polar_10.apply(get_metric, axis =1)

    # define top25
    df_polar_25 = df_polar_2.copy()
    df_top = df.iloc[:25]
    df_polar_25['value'] = df_polar_25.apply(get_metric, axis =1)

    # define top50
    df_polar_50 = df_polar_2.copy()
    df_top = df.iloc[:50]
    df_polar_50['value'] = df_polar_50.apply(get_metric, axis =1)

    # define top100
    df_polar_100 = df_polar_2.copy()
    df_top = df.iloc[:100]
    df_polar_100['value'] = df_polar_100.apply(get_metric, axis =1)

    # define top all
    df_polar_all = df_polar_2.copy()
    df_top = df
    df_polar_all['value'] = df_polar_all.apply(get_metric, axis =1)

    # draw audio profile per top N
    df_polar_compare = pd.concat([df_polar_2.loc[df_polar_2['metric']=="mean"], 
                                df_polar_10.loc[df_polar_10['metric']=="mean"],  
                                df_polar_50.loc[df_polar_50['metric']=="mean"], 
                                df_polar_all.loc[df_polar_all['metric']=="mean"]],
                                ignore_index=True)
    df_polar_compare['top N'] = ['top2', 'top2','top2','top2','top2','top2','top2', 
                                'top10', 'top10','top10','top10','top10','top10','top10',
                                'top50', 'top50','top50','top50','top50','top50','top50',
                                'top1000','top1000','top1000','top1000','top1000','top1000','top1000']
    
    fig_polar = px.line_polar(df_polar_compare, 
              r='value', 
              theta='audio_feature', 
              color='top N', 
              line_close=True, 
              title = 'Audio profiles per TOP N') 
    st.plotly_chart(fig_polar)

    # part focusing on top Ns
    st.header("Focus on TOP 2")
    fig_polar = px.line_polar(df_polar_2, 
              r='value', 
              theta='audio_feature', 
              color='metric', 
              line_close=True, 
              title = 'TOP2 tracks audio profile') 
    st.plotly_chart(fig_polar)

    st.header("Focus on TOP 10")
    fig_polar = px.line_polar(df_polar_10, 
              r='value', 
              theta='audio_feature', 
              color='metric', 
              line_close=True, 
              title = 'TOP10 tracks audio profile') 
    st.plotly_chart(fig_polar)

    st.header("Focus on TOP 25")
    fig_polar = px.line_polar(df_polar_25, 
              r='value', 
              theta='audio_feature', 
              color='metric', 
              line_close=True, 
              title = 'TOP25 tracks audio profile') 
    st.plotly_chart(fig_polar)

    st.header("Focus on TOP 50")
    fig_polar = px.line_polar(df_polar_50, 
              r='value', 
              theta='audio_feature', 
              color='metric', 
              line_close=True, 
              title = 'TOP50 tracks audio profile') 
    st.plotly_chart(fig_polar)

    st.header("Focus on TOP 100")
    fig_polar = px.line_polar(df_polar_100, 
              r='value', 
              theta='audio_feature', 
              color='metric', 
              line_close=True, 
              title = 'TOP100 tracks audio profile') 
    st.plotly_chart(fig_polar)
    
    st.header("Focus on TOP 1000")
    fig_polar = px.line_polar(df_polar_all, 
              r='value', 
              theta='audio_feature', 
              color='metric', 
              line_close=True, 
              title = 'All tracks audio profile') 
    st.plotly_chart(fig_polar)

# ################# TAB 3 #################
with tab3:
    st.title("Detailed analysis")

    st.header('Overview of most successful songs, by number of spotify streams')
    text_1 = "Most streamed tracks have between **150M and 700M** streams on Spotify, with a median at **290M** streams. \nThe distribution's average is at 514M streams, highly skewed by the top-performing tracks, **max** being at **4 Bn** views."
    st.write(text_1)

    fig = px.histogram(df['streams'], title='Distribution of nb of streams')
    st.plotly_chart(fig)

    # st.header("BPM")
    # st.markdown("Most popular songs have a BPM between 100 and 140, with a median/mean at around 121. The TOP10 tracks range between 90 and 186, about half above average, and the other half below. This indicates indeed that BPM is not a significant factor to predict a track's success, although it is a safe choice to be within the standard range mentioned above. - We will deep dive more into this audio feature when looking at the genre.")
    df_top10=df.iloc[:10]   

    st.header("Danceability - details")
    st.markdown("Most popular songs are very suitable for dancing, with a danceability between 60 and 80%, and a mean/median around 68%. However, contrary to instrumentalness and speechiness which had a very narrow range, danceability has a broader range, with some TOP3 songs having a danceability lower than average, at 50% ('Blinding lights', 'Someone you loved')")

    fig = px.histogram(df['danceability_%'], title='Distribution of danceability', nbins=30)
    st.plotly_chart(fig)
    fig = px.box(df['danceability_%'], title='Distribution of danceability')
    fig.show()
    st.plotly_chart(fig)
    
    df_line_mean_dance = pd.Series(np.full(10, df['danceability_%'].mean()))
    df_line_median_dance = pd.Series(np.full(10, df['danceability_%'].median()))

    fig = px.bar(x=df_top10['track_name']+' ('+df_top10['artist(s)_name']+')', 
                y=df_top10['danceability_%'], 
                labels={'x':'track name', 'y':'danceability'})
    fig.add_traces(go.Scatter(x=df_top10['track_name']+' ('+df_top10['artist(s)_name']+')', 
                            y=df_line_mean_dance, 
                            mode = 'lines', 
                            marker_color='orange',
                            name="danceability mean"))
    fig.add_traces(go.Scatter(x=df_top10['track_name']+' ('+df_top10['artist(s)_name']+')', 
                            y=df_line_median_dance, 
                            mode = 'lines', 
                            marker_color='blue',
                            name="danceability median"))
    fig.update_layout(height=600, title='Danceability for the TOP10 tracks, compared to mean and median')
    st.plotly_chart(fig)

    st.header("Speechiness - details")
    st.markdown("Most popular songs have a low speechiness, between 4-11% (median: 6%), which can be considered as almost with no spoken words. Note that the mean (10%) is skewed by several outliers with higher speechiness. ")
    
    st.markdown("### Focus on TOP10 Speechiness")

    st.header("Valence - details")
    st.markdown("Valence distribution is quite even and symmetrical around the mean/median 51%. Most values are between 32% and 70%. Popular songs can either have high valence and convey positive energy, or have low valence, conveying sad vibes, as well as neutral valence. This makes sense as we tend to listen to songs in various contexts (to feel energized and pumped, comforted when sad, to focus...). We find higher and lower than average valence tracks among the TOP10, which ranges between more extreme values: from 36% to 93%.")
    
    st.markdown("### Focus on TOP10 Valence")

    st.header("Energy - details")
    st.markdown("Most popular songs have a rather high energy, between 53% and 77%. Mean and median are close, at around 65%. TOP10 tracks have values below and above average, from 41% ('Someone you love') to 80% ('Blinding lights') !")
    
    st.markdown("### Focus on TOP10 Energy")

    st.header("Acousticness - details")
    st.markdown("Most popular songs have acousticness values within a broad range from 6 to 43%, with a median at 18%. With half of the TOP10 tracks above average, and half below, this audio feature is clearly not a parameter telling us if a track will be more popular or not.")
    
    st.markdown("### Focus on TOP10 Acousticness")

    st.header("Liveness - details")
    st.markdown("Most popular songs have a low liveness, between 10-24% (median at 12%), showing studio tracks make more streams. Only 2 tracks of the TOP10 have a higher liveness than average with 'One Dance' achieving even 35%. However, those are all studio tracks, and almost no popular song is live (only 5 tracks, i.e. 0.5% have a liveness >80%).")
    
    st.markdown("### Focus on TOP10 Liveness")

    st.header("Instrumentalness - not considered?")
    st.markdown("Most popular songs contain vocals (0% instrumentalness). The TOP10 songs are 100% vocal. This makes sense with the speechiness % analyzed above: popular songs have vocals, but not too much.")
