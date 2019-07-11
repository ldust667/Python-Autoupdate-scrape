#!/usr/bin/env python3

import bs4
import requests
from bs4 import BeautifulSoup as soup
from urllib2 import urlopen as uReq
import urllib
myUrl= "https://www.games-workshop.com/en-US/Orks-Warboss-Grukks-Boss-Mob-2018"
#opening and grabbing the page
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64)' 'AppleWebKit/537.11 (KHTML, like Gecko) ' 'Chrome/23.0.1271.64 Safari/537.11', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3', 'Accept-Encoding': 'none', 'Accept-Language': 'en-US,en;q=0.8', 'Connection': 'keep-alive'}
#converting variable to be readable by method below








'''
headers = urllib.urlencode(headers)
try:
	
	uClient = uReq(myUrl, headers, timeout=5)    
# your logic is here

except requests.ConnectionError as e:
    	print("OOPS!! Connection Error. Make sure you are connected to Internet. Technical Details given below.\n")
    	print(str(e))
except requests.Timeout as e:
    	print("OOPS!! Timeout Error")
    	print(str(e))
except requests.RequestException as e:
    	print("OOPS!! General Error")
    	print(str(e))
except KeyboardInterrupt:
    	print("Someone closed the program")

pageHtml = uClient.read()
uClient.close()

pageSoup = soup(pageHtml, "html.parser")

print pageSoup.p

'''
