"""
Our data is presented as a SQLite database file. To deal with our data in a simpler
way, we will use the sqlite3 library to load the data into a pandas DataFrame.
"""

import sqlite3
import pandas as pd

# Initialize an empty dictionary to store the data
simple_data = {}

# Create a connection to the database file  (anos_jobs.db3)
connection = sqlite3.connect('C:\\Users\\nouro\Desktop\\anon_jobs.db3')
cursor = connection.cursor()

# Query the table schema to get column names
cursor.execute("PRAGMA table_info(jobs)")
columns_info = cursor.fetchall()
column_names = [column[1] for column in columns_info]

# Query the table for all rows
cursor.execute("SELECT * FROM jobs")
rows = cursor.fetchall()

# Adding columns to the dictionary
for column_name in column_names:
    simple_data[column_name] = []

# Adding rows to the dictionary
for row in rows:
    for i in range(len(row)):
        simple_data[column_names[i]].append(row[i])

# Close the connection
cursor.close()
connection.close()

# Convert the dictionary to a pandas DataFrame
simple_data = pd.DataFrame(simple_data)

# Save as a CSV file to be used for later analysis and prediction
simple_data.to_csv('data/anon_jobs.csv', index=False)