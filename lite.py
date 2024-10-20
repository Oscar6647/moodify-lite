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
    def Happy(uri):
        #Grabs ID for Liked Songs
        print ('\n', "Grabbing the Happy songs on repeat songs id")
        results = sp.playlist(uri)
        for idx, item in enumerate(results['tracks']['items']):
            trackta.append(item['track']['id'])
        for idx, item in enumerate(trackta):
            metrics=sp.audio_features(trackta[idx])
            if(metrics[0]['valence']>0.5 and metrics[0]['energy']>0.5 ):
                    happy.append(trackta[idx])if trackta[idx] not in happy else happy

    def Sad(uri):
        #Grabs ID for Liked Songs
        print ('\n', "Grabbing the Sad songs on repeat songs id")
        results = sp.playlist(uri)
        for idx, item in enumerate(results['tracks']['items']):
            trackta.append(item['track']['id'])
        for idx, item in enumerate(trackta):
            metrics=sp.audio_features(trackta[idx])
            if(metrics[0]['valence']<0.5 and metrics[0]['energy']<0.5 ):
                    happy.append(trackta[idx])if trackta[idx] not in sad else sad
                


    
    def Angry(uri):
            #Grabs ID for Liked Songs
        print ('\n', "Grabbing the Angry on repeat songs id")
        results = sp.playlist(uri)
        for idx, item in enumerate(results['tracks']['items']):
            trackta.append(item['track']['id'])
        for idx, item in enumerate(trackta):
            metrics=sp.audio_features(trackta[idx])
            if(metrics[0]['valence']<0.5 and metrics[0]['energy']>0.5 ):
                angry.append(trackta[idx])if trackta[idx] not in angry else angry



    def Calm(uri):
        #Grabs ID for Liked Songs
        print ('\n', "Grabbing the Calm on repeat songs id")
        results = sp.playlist(uri)
        for idx, item in enumerate(results['tracks']['items']):
            trackta.append(item['track']['id'])
        for idx, item in enumerate(trackta):
            metrics=sp.audio_features(trackta[idx])
            if(metrics[0]['valence']<0.5 and metrics[0]['energy']>0.5 ):
                calm.append(trackta[idx])if trackta[idx] not in calm else calm
        
    def usage(uri):
        lite.Happy(uri)
        lite.Sad(uri)
        lite.Angry(uri)
        lite.Calm(uri)
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