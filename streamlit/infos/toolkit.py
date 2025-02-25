import streamlit as st

st.title("Our toolkit")

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
    st.image("./streamlit/images/pandas.png", width=80)
    st.markdown("**Pandas**")
    
with col6:
    st.image("./streamlit/images/apify.png", width=80)
    st.markdown("**Apify**")
