"""
pandas exercises with the airbnb listings data
"""

import os

import matplotlib.pyplot as plt
import pandas as pd

#%%

# load file

df = pd.read_csv(os.path.join('..', 'data', 'csv', 'listings.csv'))
print(df.head())

#%%

# overview

description = df.describe
shape = df.shape

cols = df.columns
cols_2 = list(df)

property_names = list(df['name'])
# df['name'] returns a Series object

df_nodupls = df.drop_duplicates(inplace=False)
#  inplace is important. By default set to False

#%%

# subsetting

firstrow = df.iloc[0] # equivalent to df.loc[0]
first_property_name = df.iloc[0]['name']  # equivalent to df.loc[0, 'name']
slice_property_names = df.loc[100:150, 'name']

df_small = df[['name', 'host_name', 'room_type', 'price']]

df_small_2 = df.drop(['id', 'latitude', 'longitude', 'last_review',
                      'reviews_per_month', 'calculated_host_listings_count'],
                     axis=1,
                     inplace=False)

df_sorted = df.sort_values(by=['price'], inplace=False)

hosts_unique = df['host_name'].unique()

hosts_counts = df['host_name'].value_counts()

cheap_properties = df.loc[(df['price'] > 5) & (df['price'] < 20), 'name']
# note that df['price'] < 20 would be a where condition in sql:
# SELECT name from df WHERE (price > 5 AND price < 20);

neighbourhood_mean_prices = df.groupby('neighbourhood')['price'].mean()


#%%

# plots

df.loc[(df['price'] > 5) & (df['price'] < 100), 'price'].hist()
# equivalent to: df.loc[(df['price'] > 5) & (df['price'] < 100), :].hist(column='price')
plt.show()
# plt.show() so that our figures do not overlap
 
df.groupby('host_name')['number_of_reviews'].mean().sort_values().plot()
plt.show()

series = df.groupby('host_name')['number_of_reviews'].mean().sort_values()
series_ = series[series > 300]
series_.plot(style='.-')
plt.show()

#%%

#
# Exercise:
# Which are the most common room types?
#


#%%

#
# Exercise:
# Which are the 10 most expensive properties and their neighbourhoods?
#


#%%

#
# Exercise:
# What is the maximum price each host asks for a property?
#

#%%

#
# Exercise:
# How much is the average price for a private room in the Moabit area?
# Hint: look for the string 'Moabit' in the neighbourhood names using '.str.find'
#

#%%

#
# Exercise:
# Plot the number of properties with prices under 20 € per neighbourhood.
#
