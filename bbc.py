import urllib.request
import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
 
url = "http://feeds.bbci.co.uk/news/world/rss.xml"

Client=urlopen(url)

xml_page=Client.read()
Client.close()

soup_page=soup(xml_page,"xml")
news_list=soup_page.findAll("item")

newsList=[]
for news in news_list:
	if news.pubDate in news:
		newsList.append(news)

def getFromBbc():
	return newsList