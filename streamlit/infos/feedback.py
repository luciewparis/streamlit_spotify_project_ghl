import streamlit as st
from streamlit_player import st_player
from streamlit_extras.let_it_rain import rain

global count_likes
count_likes = 0
link_cat = "https://media.giphy.com/media/ZyNQFqZLFUhr2/giphy.gif?cid=790b761105y9kyoz20oj43io96nwt4kusnms2ddvynpehptu&ep=v1_gifs_search&rid=giphy.gif&ct=g"
link_dog = "https://media.giphy.com/media/TkBoNth0Ps3Vm/giphy.gif?cid=ecf05e47vn3fc6gmplmp7crm5tn41pxjlt11pp25rauwfggj&ep=v1_gifs_search&rid=giphy.gif&ct=g"

st.subheader("Give us your feedback ❤️️")

if st.button("Nah, I'm a dog person", icon="🐶", type="secondary"):
    link_gif = ""
    if st.button("Ok, I prefer cats", icon="🐱", type="primary"):
        # st.markdown("Too late, babe")
        pass
    st.image(link_dog)
else:
    st.image(link_cat)

st.markdown("#### Please tell us if you liked our project")

sentiment_mapping = [":material/thumb_down:", ":material/thumb_up:"]
selected = st.feedback("thumbs")

if selected is not None:
    st.markdown(f"You selected: {sentiment_mapping[selected]}")
    if selected == 1: # like
        count_likes += 1
        # from: https://arnaudmiribel.github.io/streamlit-extras/extras/let_it_rain/
        st.markdown("""#### **😃 Thank you for your support!**""")
    
        st_player("https://youtu.be/3GwjfUFyY6M?si=z-syx3xxvYNb5QnC&t=24")

        rain(
            emoji="💘️",
            font_size=54,
            falling_speed=4,
            animation_length="infinite",
        )

        st.markdown(f'{sentiment_mapping[selected]} {count_likes} like(s)')

        # st.markdown("""
        #     <style>
        #     .stSlider [data-baseweb=slider]{
        #         width: 50%;
        #     }
        #     </style>
        #     """,unsafe_allow_html=True)
        # rating = st.slider("Rate your interest in knowing more about our further analyses (0 = not interested 👎 , 5 = totally in love 👍)", 
        #                         min_value=1, 
        #                             max_value=5)
        # st.write("My interest level is", rating)

        # if rating < 3:
        #     st.write("*Try again*")
        # else:
        #     if st.button("Send", type="primary"):
                

    else:
        rain(
            emoji="😢",
            font_size=54,
            falling_speed=4,
            animation_length="infinite",
        )
        st.markdown("#### 😥**We're sorry you did not like our project. Bye bye.**")
        
        st_player("https://youtu.be/Eo-KmOd3i7s?si=OUYHrPI1gG0XXzx6&t=20")
        


                


