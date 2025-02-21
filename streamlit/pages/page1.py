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
    st.title("Definitions of the 8 audio features used for our analysis")


    st.header("1. Danceability 💃")
    st.markdown("""Danceability describes **how suitable a track is for dancing** based on a combination of musical elements including tempo, rhythm stability, beat strength, and overall regularity. 
                A value of 0.0 is least danceable and 100% is most danceable.""")
    st.markdown("Example of a track with **high danceability (96%)**: #511")
    st_player("https://youtu.be/pekzpzNCNDQ?si=WpQ-nqNY1GBOdtZA&t=68")
    st.markdown("Example of a track with *low danceability (23%)*: #372")
    st_player("https://www.youtube.com/watch?v=v5ryZdpEHqM&t=9s")

    st.header("2. Speechiness 🗣")
    st.markdown("""Speechiness detects the **presence of spoken words** in a track. 
                The more exclusively speech-like the recording (e.g. talk show, audio book, poetry), the closer to 100% the attribute value. Values above 0.66 describe tracks that are probably made entirely of spoken words. Values between 33% and 66% describe tracks that may contain both music and speech, either in sections or layered, including such cases as rap music. Values below 33% most likely represent music and other non-speech-like tracks.""")
    st.markdown("Example of a track with **high Speechiness (64%)**: #856 ")
    st_player("https://youtu.be/OZgQnRcGZXs?si=2znKGsUTzCvjPXUt&t=63")
    st.markdown("Example of a track with *low Speechiness (2%)*: this track at position #61 has half the amount of lyrics of the above track")
    st_player("https://youtu.be/RB-RcX5DS5A?si=EzygWpobFxjUylIt")

    st.header("3. Valence ☀️")
    st.markdown("""A measure from 0.0 to 100% describing the **musical positiveness** conveyed by a track. 
                Tracks with high valence sound more positive (e.g. happy, cheerful, euphoric), while tracks with low valence sound more negative (e.g. sad, depressed, angry).""")
    st.markdown("Example of a track with **high Valence (97%)**: #50")
    st_player("https://youtu.be/dT2owtxkU8k?si=uEEVtwgJMZaReGcl&t=61")
    st.markdown("Example of a track with *low Valence (4%)*: #248")
    st_player("https://youtu.be/sVx1mJDeUjY?si=95YACnVJdXILYP3E&t=46")

    st.header("4. Energy 💪")
    st.markdown("""Energy is a measure from 0 to 100 and represents a perceptual **measure of intensity and activity**. 
                Typically, energetic tracks feel fast, loud, and noisy. For example, death metal has high energy, while a Bach prelude scores low on the scale. Perceptual features contributing to this attribute include dynamic range, perceived loudness, timbre, onset rate, and general entropy.""")
    st.markdown("Example of a track with **high Energy (97%)**: #337")
    st_player("https://youtu.be/w-sQRS-Lc9k?si=mSzmTEIok50eIBSE&t=16")
    st.markdown("Example of a track with *low Energy (9%)*: #941")
    st_player("https://youtu.be/cW8VLC9nnTo?si=KvrQU423ch8OrYJF&t=8")

    st.header("5. Acousticness 🎸")
    st.markdown("""A **confidence measure** from 0 to 100 of** whether the track is acoustic**. 
                100% represents high confidence the track is acoustic.""")
    st.markdown("Example of a track with **high Acousticness (97%)**: #83")
    st_player("https://youtu.be/KtlgYxa6BMU?si=mmUDpp8ZXBn-FGn-&t=27")
    st.markdown("Example of a track with *low Acousticness (0%)*: #34")
    st_player("https://youtu.be/tvTRZJ-4EyI?si=X2YEiJXjHDZxM2gU&t=7")

    st.header("6. Liveness 🎤")
    st.markdown("""Detects the **presence of an audience** in the recording. 
                Higher liveness values represent an increased probability that the track was performed live. A value above 80% provides strong likelihood that the track is live.""")
    # st.markdown("Comparing tracks with different levels of instrumentalness and seeing the low impact of this feature on a track's success, we will not consider this audio feature as we do not find it insightful for our analysis.")
    st.markdown("Example of a track with **high Liveness (97%)**: #506")
    st_player("https://youtu.be/r2ma8WPRppk?si=ZcG8nV_wlHvk5qFD&t=3")
    st.markdown("Example of a track with *low Liveness (3%)*: #579")
    st_player("https://youtu.be/8dJyRm2jJ-U?si=p3cIwh0yYFtv1yKL&t=58") 

    st.header("7. Instrumentalness 🎼 - not considered for profiling (too uncertain)")
    st.markdown("""A **confidence measure** predicting whether a track contains **no vocals**. 
                'Ooh' and 'aah' sounds are treated as instrumental in this context. Rap or spoken word tracks are clearly 'vocal'. The closer the instrumentalness value is to 100%, the greater likelihood the track contains no vocal content. Values above 50% are intended to represent instrumental tracks, but confidence is higher as the value approaches 100%.""")
    # st.markdown("Comparing tracks with different levels of instrumentalness and seeing the low impact of this feature on a track's success, we will not consider this audio feature as we do not find it insightful for our analysis.")
    st.markdown("Example of a track with **high Instrumentalness (91%)**: #392")
    st_player("https://youtu.be/V8fYAAh5uuA?si=Bc-j6F34cU6bpmC2&t=36")
    st.markdown("Example of a track with *low Instrumentalness (0%)*: #1")
    st_player("https://youtu.be/4NRXx6U8ABQ?si=Id0ZtDRkjwR-Ue3h&t=73")

    st.header("8. BPM 🎧 - not considered for profiling (too uncertain)")
    st.markdown("""The overall **estimated tempo** of a track in beats per minute (BPM). 
                In musical terminology, tempo is the **speed** or pace of a given piece and derives directly from the average beat duration.""")
    st.markdown("Example of a track with **high BPM (180)**: not in the top tracks but for reference only")
    st_player("https://youtu.be/wiBXrkka-YA?si=4N6fKFnGL2SPRp1o&t=94")
    st.markdown("Example of a track with *low BPM (65)*: #781")
    st_player("https://youtu.be/npu0F7n4M9Y?si=iVMLN7uPJTGKVkuR&t=12")

# ################# TAB 2 #################
with tab2:
    st.title("What are the audio features of successful tracks in 2023?")

   # Get initial data
    df = pd.read_csv('./data/2023_Most_Streamed_clean_api_genre.csv') # path should be relative to the root

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
    # and conclude

    # Context (for comparing TOP2 vs others)
    st.markdown("")

    # Takeaways for audio profile
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

    st.markdown("""
                
    Overall popular tracks have 
    - very **high** danceability 💃
    - very **high** valence (positive vibes) ☀️
    - very **high** energy 💪
    - and a very **low** acousticness 🎸
    - a very **low** liveness 🎤
    - a very **low** speechiness (not too many lyrics) 🗣
    - and are not fully instrumental at all 🎼
    """)
           
    st.markdown("It seems that the **most popular** tracks (as in most streamed) have the **most extreme values** e.g. highest danceability + lowest liveness")


    # part focusing on top Ns
    st.header("Focus on TOP 2")
    st.markdown("The range for the different audio features is however quite broad.")
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
    df_top10=df.iloc[:10]   

    st.header("Approach details")
    st.markdown("The analysis has been conducted on the **TOP 1000 most streamed songs as of end of year 2023**. It is a different dataset than the one used for the other sections, that use a more recent dataset. Spotify API however no longer provides audio features information since 2024.")

    st.info(
        "Note that **no strong correlation was found between the audio features and the number of streams**, resulting in quite similar patterns for most tracks of the TOP 1000 (number of tracks in our dataset)."
    )

    # plt.figure(figsize=(15,15))
    # fig = sns.heatmap(df[['streams','speechiness_%', 'danceability_%', 'liveness_%', 'instrumentalness_%', 'valence_%', 'energy_%', 'acousticness_%', 'bpm']] .corr(),    
    #         annot=True)
    # st.pyplot(fig)
    image_path = "./streamlit/images/correlation_matrix.png" 
    st.image(image_path)

    st.markdown("The strongest correlation for number of streams is with speechiness, with -0.11% only.")

    st.header("Danceability - details")
    st.markdown("Most popular songs are **very suitable for dancing, with a danceability between 60 and 80%**, and a mean/median around **68%**. However, contrary to instrumentalness and speechiness which had a very narrow range, danceability has a broader range, with some TOP3 songs having a danceability lower than average, at 50% ('Blinding lights', 'Someone you loved')")

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
    st.markdown("Most popular songs have a **low speechiness, between 4-11% (median: 6%)**, which can be considered as almost with no spoken words. Note that the mean (10%) is skewed by several outliers with higher speechiness. ")
    
    fig = px.histogram(df['speechiness_%'], title='Distribution of speechiness')
    st.plotly_chart(fig)

    fig = px.box(df['speechiness_%'], title='Distribution of speechiness')
    st.plotly_chart(fig)

    df_line_mean_speech = pd.Series(np.full(10, df['speechiness_%'].mean()))
    df_line_median_speech = pd.Series(np.full(10, df['speechiness_%'].median()))

    fig = px.bar(x=df_top10['track_name']+' ('+df_top10['artist(s)_name']+')', 
                y=df_top10['speechiness_%'], 
                labels={'x':'track name', 'y':'speechiness'})

    fig.add_traces(go.Scatter(x=df_top10['track_name']+' ('+df_top10['artist(s)_name']+')', 
                            y=df_line_mean_speech, 
                            mode = 'lines', 
                            marker_color='orange',
                            name="speechiness mean"))

    fig.add_traces(go.Scatter(x=df_top10['track_name']+' ('+df_top10['artist(s)_name']+')', 
                            y=df_line_median_speech, 
                            mode = 'lines', 
                            marker_color='blue',
                            name="speechiness median"))


    fig.update_layout(height=600, title='Speechiness for the TOP10 tracks, compared to mean and median')
    st.plotly_chart(fig)

    st.header("Valence - details")
    st.markdown("Valence distribution is quite even and symmetrical around the **mean/median 51%**. Most values are **between 32% and 70%**. Popular songs can either have high valence and convey positive energy, or have low valence, conveying sad vibes, as well as neutral valence. This makes sense as we tend to listen to songs in various contexts (to feel energized and pumped, comforted when sad, to focus...). We find higher and lower than average valence tracks among the TOP10, which ranges between more extreme values: from 36% to 93%.")

    fig = px.histogram(df['valence_%'], title='Distribution of valence')
    st.plotly_chart(fig)

    fig = px.box(df['valence_%'], title='Distribution of valence')
    st.plotly_chart(fig)

    df_line_mean_valence = pd.Series(np.full(10, df['valence_%'].mean()))
    df_line_median_valence = pd.Series(np.full(10, df['valence_%'].median()))

    fig = px.bar(x=df_top10['track_name']+' ('+df_top10['artist(s)_name']+')', 
                y=df_top10['valence_%'], 
                labels={'x':'track name', 'y':'valence'})

    fig.add_traces(go.Scatter(x=df_top10['track_name']+' ('+df_top10['artist(s)_name']+')', 
                            y=df_line_mean_valence, 
                            mode = 'lines', 
                            marker_color='orange',
                            name="valence mean"))

    fig.add_traces(go.Scatter(x=df_top10['track_name']+' ('+df_top10['artist(s)_name']+')', 
                            y=df_line_median_valence, 
                            mode = 'lines', 
                            marker_color='blue',
                            name="valence median"))

    fig.update_layout(height=600, title='Valence for the TOP10 tracks, compared to mean and median')
    st.plotly_chart(fig)

    st.header("Energy - details")
    st.markdown("Most popular songs have a rather **high energy, between 53% and 77%**. Mean and median are close, at around **65%**. TOP10 tracks have values below and above average, from 41% ('Someone you love') to 80% ('Blinding lights') !")
    
    fig = px.histogram(df['energy_%'], title='Distribution of energy')
    st.plotly_chart(fig)

    fig = px.box(df['energy_%'], title='Distribution of energy')
    st.plotly_chart(fig)

    df_line_mean_energy = pd.Series(np.full(10, df['energy_%'].mean()))
    df_line_median_energy = pd.Series(np.full(10, df['energy_%'].median()))

    fig = px.bar(x=df_top10['track_name']+' ('+df_top10['artist(s)_name']+')', 
                y=df_top10['energy_%'], 
                labels={'x':'track name', 'y':'energy'})

    fig.add_traces(go.Scatter(x=df_top10['track_name']+' ('+df_top10['artist(s)_name']+')', 
                            y=df_line_mean_energy, 
                            mode = 'lines', 
                            marker_color='orange',
                            name="energy mean"))

    fig.add_traces(go.Scatter(x=df_top10['track_name']+' ('+df_top10['artist(s)_name']+')', 
                            y=df_line_median_energy, 
                            mode = 'lines', 
                            marker_color='blue',
                            name="energy median"))


    fig.update_layout(height=600, title='Energy for the TOP10 tracks, compared to mean and median')
    st.plotly_chart(fig)

    st.header("Acousticness - details")
    st.markdown("Most popular songs have acousticness values within a broad range **from 6 to 43%, with a median at 18%**. With half of the TOP10 tracks above average, and half below, this audio feature is clearly not a parameter telling us if a track will be more popular or not.")

    fig = px.histogram(df['acousticness_%'], title='Distribution of acousticness')
    st.plotly_chart(fig)

    fig = px.box(df['acousticness_%'], title='Distribution of acousticness')
    st.plotly_chart(fig)

    df_line_mean_acoustic = pd.Series(np.full(10, df['acousticness_%'].mean()))
    df_line_median_acoustic = pd.Series(np.full(10, df['acousticness_%'].median()))

    fig = px.bar(x=df_top10['track_name']+' ('+df_top10['artist(s)_name']+')', 
                y=df_top10['acousticness_%'], 
                labels={'x':'track name', 'y':'acousticness'})

    fig.add_traces(go.Scatter(x=df_top10['track_name']+' ('+df_top10['artist(s)_name']+')', 
                            y=df_line_mean_acoustic, 
                            mode = 'lines', 
                            marker_color='orange',
                            name="acousticness mean"))

    fig.add_traces(go.Scatter(x=df_top10['track_name']+' ('+df_top10['artist(s)_name']+')', 
                            y=df_line_median_acoustic, 
                            mode = 'lines', 
                            marker_color='blue',
                            name="acousticness median"))


    fig.update_layout(height=600, title='Acousticness for the TOP10 tracks, compared to mean and median')
    st.plotly_chart(fig)

    st.header("Liveness - details")
    st.markdown("Most popular songs have a **low liveness, between 10-24% (median at 12%)**, showing studio tracks make more streams. Only 2 tracks of the TOP10 have a higher liveness than average with 'One Dance' achieving even 35%. However, those are all studio tracks, and almost no popular song is live (only 5 tracks, i.e. 0.5% have a liveness >80%).")
    
    fig = px.histogram(df['liveness_%'], title='Distribution of liveness')
    st.plotly_chart(fig)

    fig = px.box(df['liveness_%'], title='Distribution of liveness')
    st.plotly_chart(fig)

    df_line_mean_live = pd.Series(np.full(10, df['liveness_%'].mean()))
    df_line_median_live = pd.Series(np.full(10, df['liveness_%'].median()))

    fig = px.bar(x=df_top10['track_name']+' ('+df_top10['artist(s)_name']+')', 
                y=df_top10['liveness_%'], 
                labels={'x':'track name', 'y':'liveness'})

    fig.add_traces(go.Scatter(x=df_top10['track_name']+' ('+df_top10['artist(s)_name']+')', 
                            y=df_line_mean_live, 
                            mode = 'lines', 
                            marker_color='orange',
                            name="liveness mean"))

    fig.add_traces(go.Scatter(x=df_top10['track_name']+' ('+df_top10['artist(s)_name']+')', 
                            y=df_line_median_live, 
                            mode = 'lines', 
                            marker_color='blue',
                            name="liveness median"))


    fig.update_layout(height=600, title='Liveness for the TOP10 tracks, compared to mean and median')
    st.plotly_chart(fig)

    st.header("Instrumentalness - not considered for profiling (too uncertain)")
    st.markdown("Most popular songs contain vocals (0% instrumentalness). **The TOP10 songs are 100% vocal**. This makes sense with the speechiness % analyzed above: popular songs have vocals, but not too much.")
    
    fig = px.histogram(df['instrumentalness_%'], title='Distribution of instrumentalness')
    st.plotly_chart(fig)

    fig = px.box(df['instrumentalness_%'], title='Distribution of instrumentalness')
    st.plotly_chart(fig)

    st.header("BPM - not considered for profiling (too uncertain)")
    st.markdown("Most popular songs have a BPM **between 100 and 140, with a median/mean at around 121**. The TOP10 tracks range between 90 and 186, about half above average, and the other half below. This indicates indeed that BPM is not a significant factor to predict a track's success, although it is a safe choice to be within the standard range mentioned above. - We will deep dive more into this audio feature when looking at the genre.")
    
    fig = px.histogram(df['bpm'], title='Distribution of bpm')
    st.plotly_chart(fig)

    fig = px.box(df['bpm'], title='Distribution of bpm')
    st.plotly_chart(fig)

    df_line_mean_bpm = pd.Series(np.full(10, df['bpm'].mean()))
    df_line_median_bpm = pd.Series(np.full(10, df['bpm'].median()))

    fig = px.bar(x=df_top10['track_name']+' ('+df_top10['artist(s)_name']+')', 
                y=df_top10['bpm'], 
                labels={'x':'track name', 'y':'bpm'})

    fig.add_traces(go.Scatter(x=df_top10['track_name']+' ('+df_top10['artist(s)_name']+')', 
                            y=df_line_mean_bpm, 
                            mode = 'lines', 
                            marker_color='orange',
                            name="bpm mean"))

    fig.add_traces(go.Scatter(x=df_top10['track_name']+' ('+df_top10['artist(s)_name']+')', 
                            y=df_line_median_bpm, 
                            mode = 'lines', 
                            marker_color='blue',
                            name="bpm median"))


    fig.update_layout(height=600, title='Bpm for the TOP10 tracks, compared to mean and median')
    st.plotly_chart(fig)