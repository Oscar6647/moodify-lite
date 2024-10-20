import streamlit as st
import pandas as pd
import numpy as n
import lite as lite
# Disable the submit button after it is clicked
def disable():
    st.session_state.disabled = True

# Initialize disabled for form_submit_button to False
if "disabled" not in st.session_state:
    st.session_state.disabled = False

st.set_page_config(
    page_title="Moodify-lite",
    page_icon="🎵",
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
    link = str(st.text_input(label="Paste here your Spotify On Repeat link!",max_chars=100))
    print(link)
    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit", on_click=disable, disabled=st.session_state.disabled)
    if submitted:
        # check this is a real spotify link!
        if (len(link)< 45 or link[0:45] != "https://open.spotify.com/playlist/37i9dQZF1Ep"):
            st.error("Error you inserted the wrong playlist or didn't write anything, try again!")
        else:
            with st.spinner('Analyzing your Spotify On Repeat...'):
                uri = link[34:56]
                print(uri)
                lite.lite.usage(uri)
            st.success("Check out this awesome Results! Please fill out one of our feeback forms!")
            st.link_button("Fill out the Feedback Form! (English)","https://forms.gle/bNH7LR5AXfWEodNc8")
            st.link_button("Fill out the Feedback Form! (Español)","https://forms.gle/qWCB8XeeC6vMmKd87")