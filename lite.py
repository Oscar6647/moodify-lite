import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv

load_dotenv("env\.env")
global happy, sad, angry, calm

client_ID= os.getenv("ID")
print(client_ID)
client_SECRET= os.getenv("SECRET")
redirect_url='http://localhost:9000'

scope= 'user-library-read','playlist-read-private','playlist-read-collaborative'
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_ID, client_secret= client_SECRET, redirect_uri=redirect_url, scope=scope))

happy=[]
sad = []
angry = []
calm = []

def Happy():
    #Grabs ID for Liked Songs
    print ('\n', "Grabbing the on repeat songs id")
    results = sp.playlist("37i9dQZF1Epp8KDOBzc2NY")
    for idx, item in enumerate(results['tracks']['items']):
        track = item['track']
        metrics=sp.audio_features(track['id'])
        if(metrics[0]['valence']>0.5 and metrics[0]['energy']>0.5 ):
            print(idx," ",track['name']," ",track['id']," ","Valence: ",metrics[0]['valence'],"Energy: ",metrics[0]['energy'])
            happy.append(track['id'])if track['id'] not in happy else happy
            song = track['id']
            print(song)

def Sad():
    #Grabs ID for Liked Songs
    print ('\n', "Grabbing the on repeat songs id")
    results = sp.playlist("37i9dQZF1Epp8KDOBzc2NY")
    for idx, item in enumerate(results['tracks']['items']):
        track = item['track']
        metrics=sp.audio_features(track['id'])
        if(metrics[0]['valence']<0.5 and metrics[0]['energy']<0.5 ):
            print(idx," ",track['name']," ",track['id']," ","Valence: ",metrics[0]['valence'],"Energy: ",metrics[0]['energy'])
            sad.append(track['id']) if track['id'] not in sad else sad
            song = track['id']
            print(song)
            


 
def Angry():
        #Grabs ID for Liked Songs
    print ('\n', "Grabbing the on repeat songs id")
    results = sp.playlist("37i9dQZF1Epp8KDOBzc2NY")
    for idx, item in enumerate(results['tracks']['items']):
        track = item['track']
        metrics=sp.audio_features(track['id'])
        if(metrics[0]['valence']<0.5 and metrics[0]['energy']>0.5 ):
            print(idx," ",track['name']," ",track['id']," ","Valence: ",metrics[0]['valence'],"Energy: ",metrics[0]['energy'])
            angry.append(track['id'])if track['id'] not in angry else angry
            song = track['id']
            print(song)



def Calm():
        #Grabs ID for Liked Songs
    print ('\n', "Grabbing the on repeat songs id")
    results = sp.playlist("37i9dQZF1Epp8KDOBzc2NY")
    for idx, item in enumerate(results['tracks']['items']):
        track = item['track']
        metrics=sp.audio_features(track['id'])
        if(metrics[0]['valence']>0.5 and metrics[0]['energy']<0.5 ):
            print(idx," ",track['name']," ",track['id']," ","Valence: ",metrics[0]['valence'],"Energy: ",metrics[0]['energy'])
            calm.append(track['id'])if track['id'] not in calm else calm
            song = track['id']
            print(song)

#Happy()
#Sad()
#Angry()
#Calm()
lengths = {
    "Happy": len(happy),
    "Sad": len(sad),
    "Angry": len(angry),
    "Calm": len(calm)
}

#all_lens = happy+sad+angry+calm
#print(all_lens)

#average = sum(range(len(all_lens)))/len(all_lens)

#print(average)

#mostinfluential = max(lengths,key=lengths.get)

#print(mostinfluential)

#SpotifyLibrary = {"HappySongs": happy, "SadSongs": sad,"AngrySongs": angry,"CalmSongs": calm}

def Hello():
    print("hello worldsssss")

#import json
#with open('secrettest.json', 'w', encoding='utf-8') as f:
    #json.dump(SpotifyLibrary, f, ensure_ascii=False, indent=4)
