# Motivation

We will explore Airbnb data using pandas. Exercises are proposed to the workshop participants.

# Data

The `listings.csv` file (3.57 MB) we will work with can be downloaded from [Inside Airbnb](http://data.insideairbnb.com/germany/be/berlin/2019-07-11/visualisations/listings.csv). It consists of 24437 records of airbnb listings in Berlin, compiled on 11 July, 2019. Please place it in the '../data/csv' folder.

# Code

The main script we will use is `../scripts/airbnb_listings.py`.

# Delve deeper

* [pandas documentation](https://pandas.pydata.org/pandas-docs/stable/reference/frame.html)
* [subsetting](https://www.dunderdata.com/blog/selecting-subsets-of-data-in-pandas-part-1)

* [data exploration](https://towardsdatascience.com/a-guide-to-pandas-and-matplotlib-for-data-exploration-56fad95f951c)

# Exercises

1. Which are the most common room types?

2. Which are the 10 most expensive properties and their neighbourhoods? 

3. What is the maximum price each host asks for a property?

4. How much is the average price for a private room in the Moabit area?
*Tip: look for the string `Moabit` in the neighbourhood names using `.str.find`.*

5. Plot the number of properties with prices under 20 € per neighbourhood.
