import streamlit as st

st.title("Our team - TO UPDATE @Graziella @Hind")

col1, col2, col3 = st.columns(3, gap="large")

with col1:
    st.image("https://www.kindpng.com/picc/m/52-525979_unknown-person-png-transparent-png.png", width=130)
    st.subheader("Graziella")
    st.markdown("Interested in transitioning to a career in data after a background in HR, Graziella loves discovering new artists and watching basketball games.")

with col2:
    st.image("https://media.licdn.com/dms/image/v2/D4E03AQHafSa3ez2-4w/profile-displayphoto-shrink_400_400/B4EZP12RO9GYAg-/0/1734996465215?e=1746057600&v=beta&t=v2WhpS9a0n-hKNNJnuJb9UCUM_67GL-0qtirdQtKRV0", width=130)
    st.subheader("Hind")
    st.markdown("Passionate about **project management**, **data analytics**, and **cooking**, Hind also enjoys **DIY** and **chess**. She is involved in volunteer projects, offering mathematics and physics tutoring to struggling students. She combines her professional expertise with her personal commitment.")

with col3:
    st.image("https://media.licdn.com/dms/image/v2/D4E03AQEbDbvAwEKj3Q/profile-displayphoto-shrink_400_400/profile-displayphoto-shrink_400_400/0/1718229579606?e=1746057600&v=beta&t=O_gLrwaq1ntPuyeavVEjH0HefEGiolVZDmP-es9TABc", width=130)
    st.subheader("Lucie")
    st.markdown("Passionate about **product management**, **data analytics** and **cats**, Lucie also loves **bouldering** 🧗‍♀️ (when not recovering from an injury), **knitting** 🧶 and producing **electronic music** tracks 🎹 that will **not** end up in the Top songs analyzed by other bootcamp students.")