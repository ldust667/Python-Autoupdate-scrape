#!/usr/bin/env python3

#import statements beautiful, requests, urllib2 for scrape mysql connector for database, anticaptcha to bypass captcha
from bs4 import BeautifulSoup
import requests
from forcediphttpsadapter.adapters import ForcedIPHTTPSAdapter
import urllib2, cookielib
import mysql.connector
import time
#from python_anticaptcha import AnticaptchaClient, NoCaptchaTaskProxylessTask
import cfscrape
import certifi
import urllib3


https = urllib3.PoolManager( cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())


#This method adds a certificate for processing from https adresses



#api_key = '174faff8fbc769e94a5862391ecfd010'
#site_key = '6Le-wvkSAAAAAPBMRTvw0Q4Muexq9bi0DJwx_mJ-'  # grab from site
#url = 'https://www.google.com/recaptcha/api2/demo'

cfscrape.DEFAULT_CIPHERS =  'TLS_AES_256_GCM_SHA384:TLS_AES_256_GCM_SHA384'


def updatePrice(modelUrl):

#had to create header with python to bypass security as traffic was blocked as a bot

#	hdr = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}

#	req = urllib2.Request(modelUrl, headers=hdr)

#	try:
#		page = urllib2.urlopen(req)

#	except urllib2.HTTPError, e:

#		print e.fp.read()
	#content = page.read()

	 #print content
	html = requests.Session()
	html.mount(modelUrl, ForcedIPHTTPSAdapter(dest_ip='1.2.3.4'))
	response = html.get(modelUrl  , headers={'Host': modelUrl}, verify=False) # cfscrape.create_scraper() #requests.get(modelUrl).content
  #soup =             # html.get(modelUrl) #BeautifulSoup(html, "html5lib")
	print response

db = mysql.connector.connect(
	host="localhost",
	user="waagh",
	passwd="Norest2019",
	database="prices"
)
#list refrenced by name to get url
dbContainerNamed= dict()
#list refrenced by url to get assoiciated name
dbContainerUrl= dict()

dbCursor= db.cursor()
#setting sql statement to run
urls=dbCursor.execute("Select url,names from models;")

#loop through and create a list associating the names of the models to the related url
for x in dbCursor:
#loop grabs object as an array of values , x[1] is the url of the sql record x[0] is the name, this loops and sets the value as intended
	dbContainerUrl[x[1]] = x[0]
	

#running statement again
urls=dbCursor.execute("Select url,names from models;")

#looping through creating a second list with refrence to urls to get name values function the same as above switching the values
for x in dbCursor:
	dbContainerNamed[x[0]] = x[1]


#grabbing url from named list and entering url into function above to get price and scraping webpage for each object to update database
for x in dbContainerNamed:
	#updatedPrice=updatePrice(dbContainerNamed[x])
	#print x
	updatePrice(x)
	print "Through loop"
	time.sleep(90)
#	dbCursor.execute("Update models set price_usd= " . updatedPrice[1:] .  "where names= " . dbContainer[x[1]])

			# testing print print dbContainerNamed['Ork Boyz']
			# testing print print dbContainerUrl['https://www.games-workshop.com/en-US/Ork-Boyz-2018']
