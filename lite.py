import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os
from dotenv import load_dotenv
import streamlit as st

load_dotenv("env\.env")
global happy, sad, angry, calm

client_ID= os.getenv("ID")
client_SECRET= os.getenv("SECRET")
redirect_url='http://www.google.com'


sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_ID, client_secret= client_SECRET))
trackta = []
happy=[]
sad = []
angry = []
calm = []
class lite:
    def Analisis(uri):
        # Grabs ID for Liked Songs
        print('\n', "Grabbing the Happy songs on repeat songs id")
        results = sp.playlist(uri)
        trackta = [item['track']['id'] for item in results['tracks']['items']]

        # Fetch all audio features in one API call
        metrics = sp.audio_features(trackta)
        
        for idx, feature in enumerate(metrics):
            if feature['valence'] > 0.5 and feature['energy'] > 0.5:
                if trackta[idx] not in happy:
                    happy.append(trackta[idx])
            elif(metrics[0]['valence']<0.5 and metrics[0]['energy']<0.5 ):
                    sad.append(trackta[idx])if trackta[idx] not in sad else sad
            elif(metrics[0]['valence']<0.5 and metrics[0]['energy']>0.5 ):
                angry.append(trackta[idx])if trackta[idx] not in angry else angry
            elif(metrics[0]['valence']>0.5 and metrics[0]['energy']<0.5 ):
                calm.append(trackta[idx])if trackta[idx] not in calm else calm
        
    def usage(uri):
        lite.Analisis(uri)
        lengths = {
            "Happy": len(happy),
            "Sad": len(sad),
            "Angry": len(angry),
            "Calm": len(calm)
        }
        all_lens = happy+sad+angry+calm
        #print(all_lens)

        average = sum(range(len(all_lens)))/len(all_lens)

        print(average)

        mostinfluential = max(lengths,key=lengths.get)

        print(mostinfluential)

        st.write(f"On Average your Ruler Cuadrant Feeling (based on your On Repeat List) is: {mostinfluential}") 
        if (mostinfluential == "Happy"):
            st.image("happy loc.png", caption= "Your Results Ilustrated!")
        elif (mostinfluential == "Sad"):
            st.image("sad loc.png",caption="Your Results Ilustrated!")
        elif (mostinfluential == "Calm"):
            st.image("calm loc.png", caption="Your Results Ilustrated!")
        else:
            st.image("angry loc.png", caption= "Your Results Ilustrated!")
#Happy()
#Sad()
#Angry()
#Calm()


#all_lens = happy+sad+angry+calm
#print(all_lens)

#average = sum(range(len(all_lens)))/len(all_lens)

#print(average)

#mostinfluential = max(lengths,key=lengths.get)

#print(mostinfluential)

#SpotifyLibrary = {"HappySongs": happy, "SadSongs": sad,"AngrySongs": angry,"CalmSongs": calm}

def Hello():
    print("hello worldsssss")

def test():
    print("test")
#import json
#with open('secrettest.json', 'w', encoding='utf-8') as f:
    #json.dump(SpotifyLibrary, f, ensure_ascii=False, indent=4)