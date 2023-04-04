import spotipy
import os
from spotipy.oauth2 import SpotifyClientCredentials
from pprint import pprint
from colorama import Fore, Back, Style
from searchyt import Downloader
import time
print(Fore.GREEN,"""
    888b     d888 8888888b.   .d8888b.  8888888888 Y88b   d88P
    8888b   d8888 888   Y88b d88P  Y88b 888         Y88b d88P
    88888b.d88888 888    888      .d88P 888          Y88o88P
    888Y88888P888 888   d88P     8888"  8888888       Y888P
    888 Y888P 888 8888888P"       "Y8b. 888            888
    888  Y8P  888 888        888    888 888            888
    888   "   888 888        Y88b  d88P 888            888
    888       888 888         "Y8888P"  888            888
    
""")

print(Fore.RESET)
print("https://github.com/efeakaroz13")
print("Author: ",Fore.CYAN,"Efe Akaröz",Fore.RESET)
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
    try:
        Downloader.downloadvideo(str(r['track']['name'])+" "+str(r['track']['artists'][0]['name']),data=r['track'])
    except Exception as e:
        print(e)
        time.sleep(10)
        try:
            Downloader.downloadvideo(str(r['track']['name'])+" "+str(r['track']['artists'][0]['name']),data=r["track"])

        except:
            continue



