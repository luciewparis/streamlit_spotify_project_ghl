import streamlit as st

st.title("Our data toolkit")
    
st.header("Datasets")
col1, col2 = st.columns(2)
with col1:
    st.markdown("*Audio analysis*")
    st.markdown("➡️ Dataset 2023: [🔗 Kaggle](https://www.kaggle.com/datasets/nelgiriyewithana/top-spotify-songs-2023)")

with col2:
    st.markdown("*Social networks & artist analyses*")
    st.markdown("➡️ Dataset 2024: [🔗 Kaggle](https://www.kaggle.com/datasets/nelgiriyewithana/most-streamed-spotify-songs-2024)")


st.header("Tools")
col1, col2, col3 = st.columns(3, vertical_alignment="bottom")

with col1:
    st.image("https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg", width=80)
    st.markdown("**Python**")

with col2:
    st.image("https://streamlit.io/images/brand/streamlit-mark-color.png", width=100)
    st.markdown("\n\n\n")
    st.markdown("**Streamlit**")

with col3:
    st.image("https://miro.medium.com/max/1400/1*AKTxXEEeVJXbl734JGsJJQ.png", width=140)
    st.markdown("**Spotify API**")

col4, col5, col6 = st.columns(3, vertical_alignment="bottom")

with col4:
    st.markdown("\n")
    st.image("https://upload.wikimedia.org/wikipedia/commons/8/84/Matplotlib_icon.svg", width=80)
    st.markdown("**Matplotlib**")

with col5:
    st.markdown("\n")
    st.image("https://seaborn.pydata.org/_images/logo-mark-lightbg.svg", width=80)
    st.markdown("**Seaborn**")
    
with col6:
    st.markdown("\n")
    st.image("./streamlit/images/apify.png", width=140)
    st.markdown("**Apify**")

col7, col8, col9 = st.columns(3, vertical_alignment="bottom")

with col7:
    st.markdown("\n\n\n")
    st.image("https://media.proglib.io/wp-uploads/2019/07/plotly.png", width=130)
    st.markdown("**Plotly**")

with col8:
    st.markdown("\n\n\n")
    st.image("./streamlit/images/pandas.png", width=100)
    st.markdown("**Pandas**")
    
# with col9:
    #st.image("./streamlit/images/apify.png", width=80)
    #st.markdown("****")
