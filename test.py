import streamlit as st
import pandas as pd
import numpy as n
import env.lite as lite

st.set_page_config(
    page_title="test",
    page_icon="👋",
)

st.write("# Moodify-Lite")

st.sidebar.warning("This is under construction, thanks for your patience!")


st.markdown(
    """
    Moodify-Lite is a lightweight version of Moodify (A Smart music recommendation system that analyzes users' voices to detect 
    their emotions and provide appropriate song recommendations.) Moodify Lite will acess your Spotify's On Repeat Playlist
    and based on the songs inside of it, analyze it, give out the emotion that you have experienced on average
    during the last 2 days.
    ### How do I use it?
    1. Open Spotify
    2. Go to your On Repeat Playlist
    3. Click on the three dots
    4. Click on Share
    5. Click on Copy link
    6. Paste it on the text box below
    7. SEE YOUR RESULTS!
    8. Send me a screen shot of your results!


    ### NOW YOU TRY IT!

"""
)
with st.form("my_form"):
    st.write("Inside the form")
    slider_val = st.slider("Form slider")
    checkbox_val = st.checkbox("Form checkbox")

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        lite.Hello()