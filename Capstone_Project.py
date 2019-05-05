#### Business Problem

We learned how  New York City and the city of Toronto can be segmented and clustered around their neighborhoods. Both cities are very diverse and are the financial capitals of their respective countries.One of the ideas would be to compare the neighborhoods of the two cities and determine how similar or dissimilar they are. 
Those that will be intertesed in my dicsuccion will be the investors who wants to open a restaurant, construct a school or start a company and they want to rent or buy a property estate. The purpose of this project is to help them better understand and see the geographical advantages of different districts so that they can have a best choice of all kinds of investments, and make wise decisions. we will consider factors relating to the advantages and disadvantages. 

#### Data Used
I will be using the foursquare location data and as well as the Newyork Data and also the data that has Toronto Neighbourhood and it's postal code, which I wrote as a .csv to my laptop after accomplishing the last peer group on "Segmenting and Neighbourhood in Toronto".
The Newyork data contain features like id, geometry_name, coordinates, borough, etc. The second data, which is the Toronto neighbourhood data consist of features like Postcode, Borough, Neighbourhood, latitude, and longitude.

I will be using this data for geographical analysis of neighbourhood in Toronto and Newyork. How investors can decide which neighbourhood to invest and not to. How new residence decide which to rent an apartment and why he/she should rent the apartment there, base on the amenities surrounding the area.


#### Discussion of The Background
To make good use of the foursquare location data, the labs done for New York and Toronto segmented and clustered neighborhoods gave me good examples for new ideas. Data science problems always target an audience and are meant to help a group of stakeholders solve a problem, so make sure that I explicitly describe the audience and why they would care about my problem.


#### Analysis 
From the results on New York and Toronto, the lab especially tells 10 most common venues in each district. The data set is about 2014 New York City Neighborhood Names. After transforming the data to Json files, it is easy to use Pandas to transform them into DataFrame. Then select the required data columns to appear and get the information we want. Geopy library is used to get the latitude and longitude values. With the locations the maps can be created and we will have a direct understanding of the neighborhoods and the purposed areas. The Folium library is also used to show maps on different requirements.


#### Discussion/Recommendation
Finally, different analysis on New York and Toronto will give us the related better data to start a company and choose a good place to resident in. And I hope my analysis will do good for them.This is a good start for an investor, to narrow down wherev to invest or not. This gives you an overview of an investors expectation should be when considering investing in either NewYork and Toronto


import numpy as np # library to handle data in a vectorized manner

import pandas as pd # library for data analsysis
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

import json # library to handle JSON files

#!conda install -c conda-forge geopy --yes # uncomment this line if you haven't completed the Foursquare API lab
from geopy.geocoders import Nominatim # convert an address into latitude and longitude values

import requests # library to handle requests
from pandas.io.json import json_normalize # tranform JSON file into a pandas dataframe

# Matplotlib and associated plotting modules
import matplotlib.cm as cm
import matplotlib.colors as colors

# import k-means from clustering stage
from sklearn.cluster import KMeans

#!conda install -c conda-forge folium=0.5.0 --yes # uncomment this line if you haven't completed the Foursquare API lab
import folium # map rendering library

print('Libraries imported.')

!wget -q -O 'Toronto_data.json' https://ibm.box.com/shared/static/fbpwbovar7lf8p5sgddm06cgipa2rxpe.json
print('Data downloaded!')


!wget -q -O 'newyork_data.json' https://cocl.us/new_york_dataset
print('Data downloaded!')

from geopy.geocoders import Nominatim
address = 'Toronto, CA'
geolocator = Nominatim(user_agent='capstone_project1')
location = geolocator.geocode(address)
latitude = location.latitude
longitude = location.longitude
print('The geograpical coordinate of Toronto are {}, {}.'.format(latitude, longitude))

# create map of New York using latitude and longitude values
map_toronto = folium.Map(location=[latitude, longitude], zoom_start=10)

# add markers to map
for lat, lng, borough, neighborhood in zip(df['Latitude'], df['Longitude'], df['Borough'], df['Neighbourhood']):
    label = '{}, {}'.format(neighborhood, borough)
    label = folium.Popup(label, parse_html=True)
    folium.CircleMarker(
        [lat, lng],
        radius=5,
        popup=label,
        color='blue',
        fill=True,
        fill_color='#3186cc',
        fill_opacity=0.7,
        parse_html=False).add_to(map_toronto)  
    
map_toronto


CLIENT_ID = 'putyourshere' # your Foursquare ID
CLIENT_SECRET = 'putyourshere' # your Foursquare Secret
VERSION = '20180604'
LIMIT = 30
print('Your credentails:')
print('CLIENT_ID: ' + CLIENT_ID)
print('CLIENT_SECRET:' + CLIENT_SECRET)

LIMIT = 100 # limit of number of venues returned by Foursquare API
radius = 500 # define radius
# create URL
url = 'https://api.foursquare.com/v2/venues/explore?&client_id={}&client_secret={}&v={}&ll={},{}&radius={}&limit={}'.format(
    CLIENT_ID, 
    CLIENT_SECRET, 
    VERSION, 
    neighborhood_latitude, 
    neighborhood_longitude, 
    radius, 
    LIMIT)
url

# function that extracts the category of the venue
def get_category_type(row):
    try:
        categories_list = row['categories']
    except:
        categories_list = row['venue.categories']
        
    if len(categories_list) == 0:
        return None
    else:
        return categories_list[0]['name']
    
venues = results['response']['groups'][0]['items']
    
nearby_venues = json_normalize(venues) # flatten JSON

# filter columns
filtered_columns = ['venue.name', 'venue.categories', 'venue.location.lat', 'venue.location.lng']
nearby_venues =nearby_venues.loc[:, filtered_columns]

# filter the category for each row
nearby_venues['venue.categories'] = nearby_venues.apply(get_category_type, axis=1)

# clean columns
nearby_venues.columns = [col.split(".")[-1] for col in nearby_venues.columns]

nearby_venues.head()
