# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 10:45:48 2019

@author: damian.campo
"""

# Import necessary module
from  sqlalchemy import create_engine
import os
import pandas as pd
os.chdir(r'C:\Users\damian.campo\Documents\Import-data-python\Database-engine')

# Create engine: engine
engine = create_engine('sqlite:///Chinook.sqlite')

# Save the table names to a list: table_names
table_names = engine.table_names()

# Print the table names to the shell
print(table_names)

######################## Extract -query- ALL (*) information from a table called 'Album'

# Open engine connection: con
con = engine.connect()

# Perform query: rs
rs = con.execute('SELECT * FROM Album')

# Save results of the query to DataFrame: df
df_ini = pd.DataFrame(rs.fetchall())
df_ini.columns = rs.keys()

# Close connection
con.close()

# Print head of DataFrame df
print(df_ini.head())


# Open engine in context manager
# Perform query and save results to DataFrame: df
with engine.connect() as con:
    #   Select olnly columns named LastName and Eployee
    rs = con.execute("SELECT LastName, Title FROM Employee")
    #   Take the first three rows
    df = pd.DataFrame(rs.fetchmany(size=3))
    #   Set the title of each column as the respective key 
    df.columns = rs.keys()


# Print the head of the DataFrame df
print(df.head())

# Print the length of the DataFrame df
print('The dataframe has ' + str(len(df)) + ' rows')


###################################################
# Open engine in context manager
# Perform query and save results to DataFrame: df
with engine.connect() as con:
    #   Select all information from table Employee where the EmployeeId is greater or equal to 6
    rs = con.execute('SELECT * FROM Employee WHERE EmployeeId >= 6')
    df = pd.DataFrame(rs)
    df.columns = rs.keys()

# Print the head of the DataFrame df
print(df.head())


###################################
# Open engine in context manager
with engine.connect() as con:
    rs = con.execute("SELECT * FROM Employee ORDER BY BirthDate")
    df = pd.DataFrame(rs.fetchall())

    # Set the DataFrame's column names
    df.columns = rs.keys()

# Print head of DataFrame
print(df.head())

#########################
# Execute query and store records in DataFrame with SINGLE LINE USING PANDAS, df_pandas
df_pandas = pd.read_sql_query('SELECT * FROM Album', engine)

# Print head of DataFrame
print(df_pandas.head())

print(df_pandas.equals(df_ini))


# Execute query and store records in DataFrame: df
df = pd.read_sql_query('SELECT * FROM Employee WHERE EmployeeId >= 6 ORDER BY BirthDate', engine)

# Print head of DataFrame
print(df.head())

##################################

# Open engine in context manager
# Perform query and save results to DataFrame: df
#Assign to rs the results from the following query: select all the records, extracting the Title of the record 
# and Name of the artist of each record from the Album table and the Artist table, respectively. To do so, INNER JOIN these two tables on the ArtistID column of both.
with engine.connect() as con:
    rs = con.execute('SELECT Title,Name FROM Album INNER JOIN Artist on Album.ArtistID = Artist.ArtistID')
    df = pd.DataFrame(rs.fetchall())
    df.columns = rs.keys()

# Print head of DataFrame df
print(df.head())

# Execute query and store records in DataFrame: df
df = pd.read_sql_query('SELECT * FROM PlaylistTrack INNER JOIN Track on PlaylistTrack.TrackId = Track.TrackId WHERE Milliseconds < 250000', engine)

# Print head of DataFrame
print(df.head())






