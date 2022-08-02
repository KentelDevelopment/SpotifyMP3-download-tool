
import urllib.request
import re
import time
from pytube import YouTube
import os

class Downloader:
    def downloadvideo(search):
			
        page = urllib.request.urlopen("https://www.youtube.com/results?search_query={}".format(search.replace(' ','+')))
        videoids=  re.findall(r"watch\?v=(\S{11})",page.read().decode())
        theurl = "https://youtube.com/watch?v="+videoids[0]

        yt = YouTube(theurl)
        print("DOWNLOADING | {}".format(yt.title))
        
        video = yt.streams.filter(only_audio=True).first()
        
        
        out_file = video.download(output_path="./static")
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)
        print("COMPLETE | {}".format(yt.title))


