"""
This file uses geopandas to examine the coordinates of airbnb properties in Berlin
"""

import os

import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd


def get_price_color(price: int) -> str:
    """ Returns a darker color hex code with a greater price"""
    if price <= 50:
        return '#fcae91'
    elif 50 < price <= 100:
        return '#fb6a4a'
    elif 100 < price <= 150:
        return '#de2d26'
    elif 150 < price <= 200:
        return '#a50f15'
    return '#000000'


# background map
shp_filename = 'gis_osm_buildings_a_free_1.shp'
map = gpd.read_file(os.path.join('..', 'data', 'shp', 'berlin-latest-free.shp',
                                 shp_filename))

# airbnb data with property locations and prices
df = pd.read_csv(os.path.join('..', 'data', 'csv', 'listings.csv'))
gdf = gpd.GeoDataFrame(
    df, geometry=gpd.points_from_xy(df['longitude'], df['latitude']))

# our subset
gdf_ = gdf.loc[(gdf['room_type'] == 'Entire home/apt') & (gdf['price'] > 5) & (gdf['price'] < 200), :]

# plot background map with property locations coloured by price
fig, ax = plt.subplots(figsize=(15, 15))
map.plot(ax=ax)
gdf_.plot(ax=ax, markersize=5, color=[get_price_color(x) for x in gdf_['price']])
plt.show()
