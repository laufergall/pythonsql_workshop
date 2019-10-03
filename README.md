# This repo

Code, data, and materials for my SQL Python workshop at Frauenloop, Berlin, October 7, 2019.

## Requirements

Technical requirements
* Python 3.7.4 (not tested with lower Python versions)
* [requirements.txt](requirements.txt)

Please follow this [guide](docs/get_started.md) to get python, anaconda environments, and an IDE set up.

## You will learn:

1. How to use [jupyter notebooks](notebooks/README.md). In [basics_pandas.ipynb](notebooks/basics_pandas.ipynb) we have an example of how to read, manipulate, and save a dataset. You can extend this notebook our create your own to e.g. expore data under `/data`.

2. Using pandas to explore data. Examples and exercises are provided in [exercises_airbnb_listings.md](docs/exercises_airbnb_listings.md) based on the code in [airbnb_listings.py](scripts/airbnb_listings.py).

3. SQL language, by playing with our mock movie rental service data. The doc [exercises_movie_rentals.md](docs/exercises_movie_rentals.md) together with the script [movie_rentals.py](scripts/movie_rentals.py) walk you through an example of creating and querying a sqlite database. Some [introductory notes](docs/notes_databases.md) about databases and RDBMSes can also be consulted.

4. (advanced) Install and use the GeoPandas library to work with geospatial data. We will follow [airbnb_geopandas.md](docs/airbnb_geopandas.md) and [airbnb_geopandas.py](scripts/airbnb_geopandas.py).
