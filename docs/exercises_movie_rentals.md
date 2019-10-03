# Motivation

We will use mock data of an imaginary movie streamer service to illustrate SQL basics. [Exercises](#Exercises) are proposed to the workshop participants.

# Data

Mock data under the `../data/` folder, generated with `../scripts/generate_mock_data.py`

# Code

The main script we will use is `../scripts/movie_rentals.py`.

# Database

Using the data provided, we will create 2 tables:

* users
* (movie) rentals

`users` -> `rentals` have a one-to-many relationship: each user may have many linked rentals, but each rental only has one corresponding user. In this case, we need a **foreign key** on the "many" side of the relationship linking back to the "one" side.

If we had a many-to-many relationship, a mapping/junction table would be necessary.

## Create a table 

E.g. by executing the statement: 

```sql
CREATE TABLE IF NOT EXISTS users (
    id integer PRIMARY KEY,
    first_name text NOT NULL,
    last_name text NOT NULL,
    email text,
    gender text);
```

We can verify that our table has been created by running in our terminal:

```bash
sqlite3 ../data/sqlite/test.db
.tables
.exit
```
	
## Insert data into a table 

We first read our data (e.g. from .json or from .csv) and execute the statement:

```sql
INSERT INTO table (column1,column2 ,..)
VALUES (value1,value2 ,...);
```
	
## Query our tables

Some examples of SELECT statements:


```sql

SELECT * FROM users LIMIT 10;

SELECT * FROM users ORDER BY last_name DESC LIMIT 10;

SELECT first_name, last_name FROM users WHERE last_name = 'Wiffill';

SELECT * FROM users WHERE last_name LIKE 'Ba%';

SELECT COUNT(*) FROM users WHERE last_name LIKE 'Ba%';

SELECT COUNT(*) FROM users GROUP BY gender;

SELECT first_name, last_name FROM users WHERE (gender = 'Male' AND email LIKE '%.edu');

SELECT DISTINCT year FROM rentals;

SELECT COUNT(DISTINCT year) FROM rentals;

SELECT DISTINCT title FROM rentals WHERE year > 2009;

SELECT id AS user_id, email, r.title, r.rental_timestamp
FROM users u
JOIN (SELECT user_id, title, rental_timestamp 
	FROM rentals 
	WHERE rental_timestamp > '2019-09-11' ORDER BY rental_timestamp ASC) r
ON u.id = r.user_id;

SELECT sum(cost) from rentals GROUP BY ;

SELECT strftime('%Y', rental_timestamp) from rentals;

```

## sqlite3 command shell

You can also perform queries by connecting to the database via sqlite3 command shell:

```bash
sqlite3 ../data/sqlite/movie_rentals.db
.tables
SELECT * FROM users WHERE last_name LIKE 'Ba%';
.exit
```
	
# Exercises

1. Read `mock_rentals.csv` and insert records into rentals. *Tip: use the `pd.read_csv()` and the `insert_rental()` methods*

2. Query: which 3 movies provided the largest profit overall and how much was this profit (return only 3 rows).

3. Query: how many times was each movie rented.

4. Query: how many unique movies were rented between 1st August 2015 and 15th February 2016.

5. (Bonus!) Query: considering 2016 only, how many movies did each user rent and how much did each user spend.

6. (Super Bonus!) Without using sqlite, repeat the exercises before to find out the same information from the data, based on pandas dataframes. Do you find it easier with sqlite or with pandas?
