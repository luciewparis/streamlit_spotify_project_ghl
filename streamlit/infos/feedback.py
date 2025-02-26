import streamlit as st
from streamlit_extras.let_it_rain import rain

st.subheader("Give us your feedback ❤️️")

st.image("https://media.giphy.com/media/ZyNQFqZLFUhr2/giphy.gif?cid=790b761105y9kyoz20oj43io96nwt4kusnms2ddvynpehptu&ep=v1_gifs_search&rid=giphy.gif&ct=g")

st.markdown("#### Please tell us if you liked our project")
sentiment_mapping = [":material/thumb_down:", ":material/thumb_up:"]
selected = st.feedback("thumbs")
if selected is not None:
    st.markdown(f"You selected: {sentiment_mapping[selected]}")


    if selected == 1:
        st.markdown("""
            <style>
            .stSlider [data-baseweb=slider]{
                width: 50%;
            }
            </style>
            """,unsafe_allow_html=True)
        rating = st.slider("Rate your interest in knowing more about our further analyses (0 = not interested 👎 , 5 = totally in love 👍)", 
                                min_value=1, 
                                   max_value=5)
        st.write("My interest level is", rating)

        if rating < 3:
            st.write("*Try again*")
        else:
            if st.button("Send", type="primary"):
                # from: https://arnaudmiribel.github.io/streamlit-extras/extras/let_it_rain/
                rain(
                    emoji="💘️",
                    font_size=54,
                    falling_speed=4,
                    animation_length="infinite",
                )

    else:
        st.markdown("**We're sorry you did not like our project.**")
        
        if st.button("Bye bye", type="primary"):
            rain(
                emoji="😢",
                font_size=54,
                falling_speed=4,
                animation_length="infinite",
            )

        


