import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go

st.title("What does a successful track look like in 2023?")

################# PART 1 #################
st.markdown('### 1. Overview of most successful songs, by number of spotify streams')
text_1 = "Most streamed tracks have between **150M and 700M** streams on Spotify, with a median at **290M** streams. \nThe distribution's average is at 514M streams, highly skewed by the top-performing tracks, **max** being at **4 Bn** views."
st.write(text_1)

# Get initial data
filepath = os.path.join('..', '..', 'data','2023_Most_Streamed_clean_api_genre.csv')
df = pd.read_csv(filepath)

fig = px.histogram(df['streams'], title='Distribution of nb of streams')
st.plotly_chart(fig)
