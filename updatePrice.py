#!/usr/bin/env python3

#import statements beautiful, requests, urllib2 for scrape mysql connector for database
from bs4 import BeautifulSoup
import requests
import urllib2
import mysql.connector


def updatePrice(modelUrl):

	url = modelUrl

	content = urllib2.urlopen(url).read()

	soup = BeautifulSoup(content)

	print soup.prettify()



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
					# testing print	print(dbContainerNamed[x[1]])
	

#running statement again
urls=dbCursor.execute("Select url,names from models;")

#looping through creating a second list with refrence to urls to get name values function the same as above switching the values
for x in dbCursor:
	dbContainerNamed[x[0]] = x[1]
			# testing print	print(dbContainerUrl[x[0]])


#grabbing url from named list and entering url into function above to get price and scraping webpage for each object to update database
for x in dbContainerNamed:
	#updatedPrice=updatePrice(dbContainerNamed[x])
	print x
#	dbCursor.execute("Update models set price_usd= " . updatedPrice[1:] .  "where names= " . dbContainer[x[1]])

			# testing print print dbContainerNamed['Ork Boyz']
			# testing print print dbContainerUrl['https://www.games-workshop.com/en-US/Ork-Boyz-2018']
