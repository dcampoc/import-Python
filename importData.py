# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 21:24:31 2019

@author: dcamp
"""

# Import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.pyplot as plt
import os

#   Set directory where data 'titanic_corrrupt.txt' is
os.chdir(r'C:\Users\dcamp\Documents\python-practice\import')
wd = os.getcwd()
print('The current directory is: ' + wd)

# Assign filename: file
file_1 = 'titanic_corrupt.txt'

# Import file: data
data = pd.read_csv(file_1, sep='\t', comment='#', na_values='Nothing')

# Print the head of the DataFrame
print(data.head())

# Plot 'Age' variable in a histogram
pd.DataFrame.hist(data[['Age']])
plt.xlabel('Age (years)')
plt.ylabel('count')
plt.show()


# Assign spreadsheet filename: file
file_2 = 'battledeath.xlsx'

# Load spreadsheet: xl
xls = pd.ExcelFile(file_2)

# Print sheet names
print('The sheets in ' + file_2 + ' are called: ' + str(xls.sheet_names))

# Load a sheet into a DataFrame by name: df1
df1 = xls.parse('2004')

# Print the head of the DataFrame df1 (head extracts the first 5 rows of the sheet in question)
print(df1.head())

# Load a sheet into a DataFrame by index: df2
df2 = xls.parse('2002')
# df2 = xls.parse(0)

# Print the head of the DataFrame df2 (head extracts the first 5 rows of the sheet in question)
print(df2.head())


# Parse the first sheet and rename the columns: df1
df0_mod = xls.parse(0, skiprows=[1], names=['Country', 'AAM due to War (2002)'])

# Print the head of the DataFrame df1
print(df0_mod.head())

# Parse the first column of the second sheet and rename the column: df2
df1_mod = xls.parse(1, usecols=[0], skiprows=[1], names=['Country'])

# Print the head of the DataFrame df2
print(df1_mod.head())

###################################################
print('importing a SAS file and plot a histogram'.upper())
# Import sas7bdat package 
from sas7bdat import SAS7BDAT

# Save file to a DataFrame: df_sas in a context manager
with SAS7BDAT('sales.sas7bdat') as file:
    df_sas = file.to_data_frame()

# Print the DataFrame
print(df_sas)
# Note that it is imported as a pandas object 
print(type(df_sas))

# Plot histogram of DataFrame features (pandas and pyplot already imported)
pd.DataFrame.hist(df_sas[['P']])
plt.ylabel('count')
plt.show()

###############################################
print('importing a DTA file and plot a histogram'.upper())

# Load Stata file into a pandas DataFrame: df
df = pd.read_stata('disarea.dta')

# Print the head of the DataFrame df
print(df.head())

# Plot histogram of one column of the DataFrame
pd.DataFrame.hist(df[['disa10']])
plt.xlabel('Extent of disease')
plt.ylabel('Number of countries')
plt.show()


############################################
print('importing and exploring a h5py file'.upper())
# Import packages
import numpy as np
import h5py

# Assign filename: file
file = 'LIGO_data.hdf5'

# Load file: data
data = h5py.File(file, 'r')

# Print the datatype of the loaded file
print(type(data))

# Print the keys of the file
for key in data.keys():
    print(key)

# Get the HDF5 group: group
group = data['strain']

# Check out keys of group
for key in group.keys():
    print(key)

# Set variable equal to time series data: strain
strain = data['strain']['Strain'].value

# Set number of time points to sample: num_samples
num_samples = 10000

# Set time vector
time = np.arange(0, 1, 1/num_samples)

# Plot data
plt.plot(time, strain[:num_samples])
plt.xlabel('GPS Time (s)')
plt.ylabel('strain')
plt.show()

#######################################
print('exploring a matlab file'.upper())
# Import package
import scipy.io

# Load MATLAB file: mat
mat = scipy.io.loadmat('albeck_gene_expression.mat')

# Print the datatype type of mat
print(type(mat))

# Print the keys of the MATLAB dictionary
print(mat.keys())

# Print the type of the value corresponding to the key 'CYratioCyt'
print(mat['CYratioCyt'])

# Print the shape of the value corresponding to the key 'CYratioCyt'
print(np.shape(mat['CYratioCyt']))

# Subset the array and plot it
data = mat['CYratioCyt'][25, 5:]
fig = plt.figure()
plt.plot(data)
plt.xlabel('time (min.)')
plt.ylabel('normalized fluorescence (measure of expression)')
plt.show()

