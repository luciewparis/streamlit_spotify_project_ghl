import streamlit as st
import plotly.express as px
import pandas as pd

st.title("Our methodology - GITHUB to update (readme) + NOTION to clean")

st.header("Collaboration tools")
st.markdown("We shared our code on a public Github repository, while tracking tasks on the project management tool Notion.")
col1, col2 = st.columns(2)

with col1:
    st.markdown("\n")
    st.image("./streamlit/images/github.png", width=50)
    st.markdown("[🔗 GHL Spotify Project](https://github.com/luciewparis/streamlit_spotify_project_ghl)")


with col2:
    st.markdown("\n")
    st.image("https://logovectordl.com/wp-content/uploads/2019/11/notion-labs-inc-logo-vector.png", width=100)
    st.markdown("[🔗 Notion](https://github.com/luciewparis/streamlit_spotify_project_ghl)")


st.header("Organization")

df = pd.DataFrame(
    {
        "y": ["time spent", "time spent", "time spent", "time spent"],
        "task": ["Data collection & EDA", "Data analysis", "Streamlit app", "Project management & coordination"],
        "%": [55, 15, 20, 10]
    }
)

fig = px.bar(df, x="%", y="y",
             color="task", 
             orientation='h', 
             height=300,
             # text="%",
             title='How we spent our time'
             )

st.plotly_chart(fig)

st.markdown("""
            
            - **🔎 Data collection & Exploratory Data Analysis**: this first step took us the most time. We were glad to find a lot of datasets in particular on Kaggle, but we had to spend time exploring them, identifying their differences and then deciding on which ones were the most relevant to keep for our analyses. Apart from Kaggle, we also explored other data sources such as directly querying the Spotify API, and getting data from other social network platforms (TikTok, Instagram, Twitter, Youtube) either through their API or through web scraping.
            
            - **📊 Data Analysis**: this step was quite straightforward thanks to librairies such as Matplotlib, Seaborn and Plotly. We intended to use Machine Learning as well for the project, but the low correlation scores on our features deterred us.
            
            - **🌐 Streamlit**: this step consisted in setting up our Streamlit app, deploying it and adapting our code from our Jupyter notebooks to the python scripts for our streamlit app. This included the design part, optimizing the navigation for clarity and preparing the content for the final presentation. Let alone debugging all that did not go as we first expected!
            
            - **📅 Project management & coordination**: in order to succeed, we coordinated among the three of us around separate tasks so we could each work with as few dependencies as possible, and yet towards the same goal. We tracked and documented our work and progress on Github and Notion, and did several checkpoints to share our ideas and align our findings.

""")