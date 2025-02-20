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

    st.header("BPM")

    st.header("Danceability")
    st.markdown("Danceability describes how suitable a track is for dancing based on a combination of musical elements including tempo, rhythm stability, beat strength, and overall regularity. A value of 0.0 is least danceable and 100% is most danceable.")
    
    st.markdown("Example of a track with **high danceability (96%)**: ")
    st_player("https://youtu.be/pekzpzNCNDQ?si=WpQ-nqNY1GBOdtZA&t=68")
    st.markdown("Example of a track with *low danceability (23%)*: ")
    st_player("https://youtu.be/v5ryZdpEHqM?si=0i8mFSysfXzTarGf&t=7")

    st.header("Speechiness")
    st.markdown("Speechiness detects the presence of spoken words in a track. The more exclusively speech-like the recording (e.g. talk show, audio book, poetry), the closer to 100% the attribute value. Values above 0.66 describe tracks that are probably made entirely of spoken words. Values between 33% and 66% describe tracks that may contain both music and speech, either in sections or layered, including such cases as rap music. Values below 33% most likely represent music and other non-speech-like tracks.")

    st.header("Instrumentalness")

    st.header("Valence")

    st.header("Energy")

    st.header("Acousticness")

################# TAB 2 #################
with tab2:
    st.title("What does a successful track look like in 2023?")


################# TAB 3 #################
with tab3:
    st.title("Detailed analysis")

    st.markdown('### 1. Overview of most successful songs, by number of spotify streams')
    text_1 = "Most streamed tracks have between **150M and 700M** streams on Spotify, with a median at **290M** streams. \nThe distribution's average is at 514M streams, highly skewed by the top-performing tracks, **max** being at **4 Bn** views."
    st.write(text_1)

    # Get initial data
    filepath = os.path.join('..', '..', 'data','2023_Most_Streamed_clean_api_genre.csv')
    df = pd.read_csv(filepath)

    fig = px.histogram(df['streams'], title='Distribution of nb of streams')
    st.plotly_chart(fig)