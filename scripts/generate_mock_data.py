"""
This script can be used to generate mock movie rentals data from an imaginary movie stream service
"""

import os
import pandas as pd
import random
import datetime

n_rows = 1000
max_user_id = 100

# user_id

user_ids = [random.randint(1, max_user_id)
            for _ in range(n_rows)]

# rental_timestamp

years = 3
end = datetime.datetime.now()
start = end - datetime.timedelta(days=365 * years)
rental_timestamps = [start + (end - start) * random.random()
                     for _ in range(n_rows)]

# title

df = pd.read_csv(os.path.join('..', 'data', 'csv', 'oscar_winners.csv'), sep=';')

df_samples = df.sample(n=n_rows, random_state=2302, replace=True)
titles = list(df_samples['movie'])

# year

years = list(df_samples['year'])

# cost

costs = [random.randrange(300, 400)/100
         for _ in range(n_rows)]

# write to csv

mock_data = pd.DataFrame(
    {'user_id': user_ids,
     'rental_timestamp': rental_timestamps,
     'title': titles,
     'year': years,
     'cost': costs})

mock_data.to_csv(os.path.join('..', 'data', 'csv', 'mock_rentals.csv'), sep=';')
