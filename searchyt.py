import requests
from bs4 import BeautifulSoup 
import json

search=input("Search Something:")

page = requests.get("https://www.youtube.com/results?search_query={}".format(search.replace(' ','+')))

content = str(page.content).split('ytInitialData = ')[1].split('</script')[0]
try:
	thejson = json.dumps(content)
	print("SUCCESSFULLY LOADED")
	open("out.json","w").write(thejson)
except Exception as e:
	print(content)
	print(e)
	


