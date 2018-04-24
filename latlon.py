#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 13:51:42 2018

@author: dav
"""

#MWE
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter
import cartopy.feature as cfeature

import cartopy

# Edinburgh, Glasgow, Aberdeen
lons = [-3.188267, -4.25763, -2.099075] 
lats = [55.9533, 55.86515, 57.149651]

plt.figure(figsize=(10,10))
ax = plt.axes(projection=ccrs.Mercator())
ax.coastlines('10m')

# Add grey for the land
land_10m = cfeature.NaturalEarthFeature('physical', 'land', '10m',
                                        edgecolor='face',
                                        facecolor=cfeature.COLORS['land'])

ax.add_feature(land_10m, edgecolor='gray')

ax.xaxis.set_visible(True)
ax.yaxis.set_visible(True)

ax.set_yticks([56,57,58,59], crs=ccrs.PlateCarree())
ax.set_xticks([-8, -6, -4, -2], crs=ccrs.PlateCarree())

lon_formatter = LongitudeFormatter(zero_direction_label=True, number_format='d')
lat_formatter = LatitudeFormatter()

ax.xaxis.set_major_formatter(lon_formatter)
ax.yaxis.set_major_formatter(lat_formatter)

ax.set_title(cartopy.__version__)

ax.set_extent([-8, -1.5, 55.3, 59])

plt.scatter(lons,lats,color='red', marker='o', s=80, transform=ccrs.PlateCarree(), zorder=2)
plt.savefig("cities.png")
plt.show()