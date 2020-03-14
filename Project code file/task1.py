import requests
import bs4

import geocoder

from gmplot import *

#------------------SUB-TASK 1-----------------------
#Here, Webscraping is being done. States and Union Territories are extracted from the web page and stored in states[]

req = requests.get('https://wiki.openstreetmap.org/wiki/India/Boundaries/States_and_Union_territories')
soup = bs4.BeautifulSoup(req.text,'lxml')

states=[]
for i in soup.select('td > a'):
    states.append(i.text)

#------------------End of SUB-TASK 1-----------------



#------------------SUB-TASK 2-----------------------
#Extracting the latitudes and longitudes of the states present in states[]

lat=[]
lng=[]

#An alternate for geocoding the location is the use of Google Geocoding API for which we require a API Key (Paid service)
#The following snippet code can be used incase if we have API.
# import googlemaps
# gmaps = googlemaps.Client(key='AIzaSyBEnv29kNaQM2fWl7xt4A3cmTHV3dLTMLw')
#
# for i in range (len(states)):
#     geocode_result = gmaps.geocode(states[i])
#     lat.append(geocode_result[0]['geometry']['location']['lat'])
#     lng.append(geocode_result[0]['geometry']['location']['lng'])

#Snippet code if we don't have a Google API key.
#Disadvantage: Latency (It takes few seconds for processing)
for i in range (len(states)):
     g = geocoder.osm(states[i])

     lat.append(g.osm['y'])
     lng.append(g.osm['x'])

#------------------End of SUB-TASK 2-----------------



#------------------SUB-TASK 3-----------------------
#Plotting the co-ordinates on MAP
#Here, we center the map with India's location coordinates
#For India,
#           Latitude = 20.5937 N
#           Longitude = 78.9629 E
#The third argument is related to ZOOM -- 5 was comfortable.

gmap = gmplot.GoogleMapPlotter(20.5937,78.9629, 5)

#In case, if we have a API key, we can make use of it else the map rendered will have text "For development purposes only"
#Below one is additional code line if we have a Google API Key.

#gmap.apikey = "AIzaSyC7eWCpbAtgIvVyJeYN1JzZ8V2711rNbr8"

gmap.scatter(lat, lng, 'cornflowerblue', size=50000, marker=False)

gmap.draw("task_result_map.html")

#------------------End of SUB-TASK 3-----------------