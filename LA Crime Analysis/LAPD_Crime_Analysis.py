#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
THIS IS THE CODE USED TO CLEAN THE DATASET. DROPPED RECORDS WITH NO VALUES AND REDUCED THE NUMBER OF ATTRIBUTES    
i
mport pandas as pd

df = pd.read_csv("Crime_Data_from_2010_to_Present.csv")

columns = ['DR Number','Reporting District','Crime Code','MO Codes','Premise Code','Weapon Used Code','Status Code','Crime Code 1','Crime Code 2','Crime Code 3','Crime Code 4','Address',	'Cross Street']
df.drop(columns,inplace=True,axis=1)
df = df.dropna()

df.to_csv('lacrimes.csv')


"""

import pandas as pd

df = pd.read_csv("lacrimes.csv")

df['Time Occurred'] = df['Time Occurred'].apply(lambda x: '{0:0>4}'.format(x))
df['Year'] = pd.DatetimeIndex(df['Date Occurred']).year

print ("LA Crime analysis")
print ("=================\n\n\n\n")

#Feature 1
print ("Crime analysis by years")
print ( "==================")
g = df.groupby("Year").size().to_frame(name='count')
print (g)

import matplotlib.pylab as plt
plt.plot(g)
plt.show()

#Feature 2
print ("\n\n\nCrime analysis by Areas")
print ("=======================")
h = df.groupby("Area Name").size().to_frame(name='count')
h = h.sort_values(by = 'count')
print ("\n\n\n\nSafest Neighborhoods in LA: \n\n", h.head())
print ("\n\n\n\nDangerous Neighborhoods in LA: \n\n", h.tail())


#Feature 3
print ("\n\n\nTime of day Analysis")
print ("====================")
bins = []
for i in range(0,25,4):
    o = int(i*100)
    bins.append(o)    
df['Time Occurred'] = df['Time Occurred'].astype(int)
df['Time Occurred'] = pd.cut(df['Time Occurred'],bins)
t = df.groupby("Time Occurred").size().to_frame(name='count')
t=t.sort_values(by = 'count',ascending = False)
print (t)

#Feature 4
print ("\n\n\nWeapons Used Analysis")
print ("=====================")
r = df.groupby("Weapon Description").size().to_frame(name='count')
r = r.sort_values(by = 'count',ascending = False)
print ("Most common weapon used: \n", r.head())

#Feature 5
print ("\n\n\nCrime Analysis by Victim Descent")
print ("================================")
o = df.groupby("Victim Descent").size().to_frame(name='count')
o = o.sort_values(by = 'count',ascending = False)
print (o)
 
# --- Build Map ---
#run the following commands in the terminal to install map packages
#conda update conda
#conda install -c anaconda basemap
#conda install -c pelson pyshp
print ("\n\n\nAerial View of LA Crime-Prone areas")
print ("=========================================")
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
# Data of city location (logitude,latitude) and population
# 1. Draw the map background
fig = plt.figure(figsize=(8, 8))
m = Basemap(projection='lcc', resolution='h', 
            lat_0=34.05, lon_0=-118.25,
            width=555555, height=555555)
m.shadedrelief()
m.drawcoastlines()

import pandas as pd
cities = pd.read_csv('lacrimes.csv')
lat = cities['lat'].values
lon=cities['lon'].values

# 2. scatter city data, with color reflecting crime-prone areas
m.scatter(lon, lat, latlon=True,cmap='Reds', alpha=0.5)

# --- Build Map ---
print ("\n\n\nClose up view of LA Crime-Prone Areas")
print ("===========================================")
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
# Data of city location (logitude,latitude) and population
# 1. Draw the map background
fig = plt.figure(figsize=(8, 8))
m = Basemap(projection='lcc', resolution='h', 
            lat_0=34.05, lon_0=-118.25,
            width=1E5, height=1E5)
m.drawmapboundary(fill_color="#CC9955")
m.drawcoastlines()

import pandas as pd
cities = pd.read_csv('lacrimes.csv')
lat = cities['lat'].values
lon=cities['lon'].values

# 2. scatter city data, with color reflecting crime-prone areas
m.scatter(lon, lat, latlon=True,cmap='Reds', alpha=0.5)
