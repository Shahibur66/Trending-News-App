import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen

news_url="http://rss.cnn.com/rss/edition.rss"

Client=urlopen(news_url)

xml_page=Client.read()
Client.close()

soup_page=soup(xml_page,"xml")
news_list=soup_page.findAll("item")


newsList=[]
for news in news_list:
	if news.pubDate in news:
		newsList.append(news)

def getFromCnn():
	return newsList