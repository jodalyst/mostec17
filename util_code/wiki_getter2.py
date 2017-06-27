import requests
import json
from bs4 import BeautifulSoup
to_send = "https://en.wikipedia.org/w/api.php?titles=cat&action=query&prop=extracts&redirects=1&format=json&exintro="

lat = 42.362119
lon = -71.091761
api_key = "AIzaSyCy1B52SM3NIfIjdFwM4qnfqTb-BDnhYHk"

to_send = '''https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={},{}&radius=300&key={}'''.format(lat,lon,api_key)

r = requests.get(to_send)
data = r.json()
print(data)
