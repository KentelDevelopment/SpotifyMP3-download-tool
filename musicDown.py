from SpotifyScraper.scraper import Scraper, Request
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from tkinter import * 
from selenium.webdriver.chrome.options import Options

options = Options()

root = Tk()
root.title('Kentel Search Tool')
root.geometry("500x500")

playlistUrl = Entry(root)
playlistUrl.pack()


current_label = Label(text="Started")
current_label.pack()

def download(url_):

    request = Request().request()
    scraper = Scraper(session=request)
    playlist_information = scraper.get_playlist_url_info(url=url_)
    for i in playlist_information["tracks_list"]:
        options.add_argument('--headless')
        driver = webdriver.Chrome("./chromedriver") 
        
        import youtube_dl
        driver.get(f"https://www.youtube.com/results?search_query={i['track_name'].replace(' ','+')}+-+{i['track_singer'].replace(' ','+')}")
        soup = BeautifulSoup(driver.page_source,"html.parser")
        driver.quit()
        url  = soup.find_all("a",{"id":"video-title"})[0].get('href')

        download_options = {
        'format': 'bestaudio/best',
        'outtmpl': '%(title)s.%(ext)s',
        'nocheckcertificate': True,
        'keepvideo': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192'
        }]
        }
        
        with youtube_dl.YoutubeDL(download_options) as ydl:
            ydl.download(["https://www.youtube.com"+url])
            print("Downloaded!")
        print(i)
        print("\n\n")
        global current_label
        current_label.config(text="Downloaded : "+i["track_name"])

    

enter_btn = Button(text="Download",command=lambda:download(playlistUrl.get()))
enter_btn.pack()


root.mainloop()