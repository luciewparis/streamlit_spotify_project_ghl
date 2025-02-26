# This file is to handle navigation in the app through the different pages
# ex. page names
# For more: see documentation: https://docs.streamlit.io/develop/concepts/multipage-apps/page-and-navigation    

import streamlit as st

# Home page = context
context = st.Page("context.py", title="Context", icon=":material/home:", default=True) # title and icon can be modified for each page 

# Our analysis pages
page1 = st.Page("pages/page1.py", title="Audio analysis", icon=":material/discover_tune:")
page2 = st.Page("pages/page2_Influence of Playlists and Social Networks on Streams.py", title="Social networks analysis", icon=":material/groups:")
page3 = st.Page("pages/page3.py", title="Selection of artists for a festival", icon=":material/saved_search:")

# Our info pages
toolkit = st.Page("infos/toolkit.py", title="Our toolkit", icon=":material/build:")
method = st.Page("infos/method.py", title="Our methodology", icon=":material/account_tree:")
team = st.Page("infos/team.py", title="About us", icon=":material/emoji_people:")

# Run navigation
# Without sections:
# pg = st.navigation([context, page1, page2, page3, toolkit, method, team])

# Create sections
pg = st.navigation(
        {
            "": [context],
            "Analyses": [page1, page2, page3],
            "About us": [toolkit, method, team]
        }
    )

st.set_page_config(page_title="Spotify Music Insights", layout="wide", page_icon=":material/edit:")
pg.run()


