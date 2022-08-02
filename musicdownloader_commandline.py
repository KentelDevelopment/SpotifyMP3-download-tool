import spotipy
import os
from spotipy.oauth2 import SpotifyClientCredentials
from pprint import pprint
from colorama import Fore, Back, Style
from searchyt import Downloader

theurl = input("? | Enter a Spotify playlist URL:")

try:
	theval1 = theurl.split("https://open.spotify.com/playlist/")[1]
	pl_id = f"spotify:playlist:{theval1}"
except:
	print("Err | Unknown URL")
	exit()
client_id = "a0c932b9e34b4149b8f367c5e403313e"
secretclient = "37335ef57fad4854825c67826b6a5816"
os.environ["SPOTIPY_CLIENT_ID"] =client_id
os.environ["SPOTIPY_CLIENT_SECRET"] =secretclient



sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

offset = 0

response = sp.playlist_items(pl_id,
                             offset=offset,
                             fields='items.track,total')
   
for r in response['items']:
	
    Downloader.downloadvideo(str(r['track']['name'])+" "+str(r['track']['artists'][0]['name']))





