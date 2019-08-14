from lxml import html
import requests

page = requests.get('https://gamesworkshop.com')
tree = html.fromstring(page.content)
print tree
