#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install geopy


# In[3]:


import datetime
print ("current date and time: ")
print(datetime.datetime.now())
from geopy.geocoders import Nominatim
import folium


# In[5]:


mijnVariabele = kobe(21+1)
mijnLijst = ["vilvoorde", "aalst", "halle"]
mijnTuple = (kvds, mijnpw)
mijnjSON = {"kvds", "cisco", "mijnpw", "cisco"} cisco = value


# In[9]:


import os
os.system("pip install geopy")


# In[12]:


get_ipython().system('pip install Nominatim')
import os
os.system("pip install Nominatim")


# In[21]:


from geopy.geocoders import Nominatim
import folium
#
geolocator = Nominatim(user_agent="http://biasc.be")
#### Enter city and country
#city_country = "moorsel, Belgium"
straat = "exterkenstraat, Belgium"
####
#location = geolocator.geocode(city_country)
location = geolocator.geocode(straat)
print(location.address)
devnet_lat = location.latitude
devnet_lon = location.longitude
print((devnet_lat, devnet_lon))
import datetime
print ("current date and time: ")
print(datetime.datetime.now())
#
coordinates = [devnet_lat,devnet_lon]
map = folium.Map(location=coordinates, tiles='OpenStreetMap',  zoom_start=12)
map
# save method of Map object will create a map
# saved in Downloads
#map.save("geopy_location.html")


# In[ ]:




