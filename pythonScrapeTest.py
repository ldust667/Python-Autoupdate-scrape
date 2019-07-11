#!/usr/bin/env python3

import bs4
import requests
from bs4 import BeautifulSoup as soup
from urllib2 import urlopen as uReq

myUrl= "https://www.games-workshop.com/en-US/Orks-Warboss-Grukks-Boss-Mob-2018"
#opening and grabbing the page
headers = {‘User-Agent’: ‘Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3’}
uClient = uReq(myUrl, headers)
pageHtml = uClient.read()
uClient.close()

pageSoup = soup(pageHtml, "html.parser")

print pageSoup.span

