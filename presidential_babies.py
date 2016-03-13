# IMPORT MODULES

import os
import glob
import sqlite3
import zipfile
import requests
import StringIO
import pandas as pd
import scipy.stats as ss


# DECLARE VARIABLES

data_url = 'http://www.ssa.gov/oact/babynames/state/namesbystate.zip'
zip_dir = 'LOCAL DIRECTORY'
prez_url = 'http://bit.ly/1X5LHFJ'


# DEFINE FUNCTIONS

def extract_year(df, col):
    '''Extract the year from a DataFrame column of strings denoting a date.'''
    return [i.year for i in pd.to_datetime(df[col])]

def fetch_one(q):
    '''Fetch a query's single record in float format.'''
    return float(cur.execute(q).fetchone()[0])


# DOWNLOAD DATA

resp = requests.get(data_url)
zip_obj = zipfile.ZipFile(StringIO.StringIO(resp.content))
zip_obj.extractall(path=zip_dir)


# LOAD DATA TO DATABASE

# Initialize SQLite database and a single table to store all of the state data.

# Create connection and cursor objects
con = sqlite3.connect(os.path.join(zip_dir, 'baby_names.db'))
cur = con.cursor()

# Create and format table (rewrite if necessary)
cur.execute('''DROP TABLE IF EXISTS state_data''')
cur.execute('''CREATE TABLE state_data
               (state TEXT, gender TEXT, year INT, name TEXT,  births INT)''')

# To protect memory, read the content of each file one line at a time and insert it into the table.

# List all of the text files in the zipped directory
state_files = glob.glob('{}*.TXT'.format(zip_dir))

# Iterate through all of the files identified
for fname in state_files:
    
    # Open each file
    with open(fname, 'r+') as f:
    
        # Iterate through the rows of the file
        for row in f:
        
            # Insert the data into the table
            cur.execute('INSERT INTO state_data VALUES (?, ?, ?, ?, ?)',
                        row.split(','))

# Commit the changes
con.commit()


# ANALYSIS

# Load president data as DataFrame and create columns with (1) their first names,
# (2) the year they took office, (3) the year they left office, and (4) the length of their tenure.

# Load data
prez_data = pd.read_csv(prez_url)

# Add missing datum (the date on which President Obama will leave office)
prez_data.ix[prez_data['President '] == 'Barack Obama', 'Left office '] = '1/20/2017'

# Split first names from full names and create variable
names = [i.split(' ') for i in prez_data['President ']]
prez_data['first_name'] = [i[0] for i in names]

# Replace nicknames with first names
nickname_to_firstname = {'first_name': {'Jimmy': 'James', 'Bill': 'William'}}
prez_data.replace(to_replace=nickname_to_firstname, inplace=True)

# Extract years in which office was taken and left
prez_data['took_office_year'] = extract_year(prez_data, 'Took office ')
prez_data['left_office_year'] = extract_year(prez_data, 'Left office ')

# Limit the data to presidents who took office after the earliest baby name data
min_year = cur.execute('SELECT MIN(year) FROM state_data').fetchone()[0]
prez_data = prez_data[prez_data['took_office_year'] > min_year]

# Calculate presidential tenure
prez_data['tenure'] = prez_data['left_office_year'] - prez_data['took_office_year']

# For each president, compute the ratio of newborns given his name during his administration
# to the number of newborns given the names of other presidents during this same period.
# Then, compute this ratio for the *n* years before his administration (*n* = the number of
# years of his administration). Finally, compute the difference of these two numbers.
# 
# If the difference is positive, then this is evidence in favor of our hypothesis.
# 
# For example, for Bill Clinton, the 1st ratio corresponds to the number of babies given the name
# William between 1993 and 2001 to the number of babies given the names of all other presidents
# during this same time period. The 2nd ratio correspond to the number of babies given the name
# William between 1984 and 1992 to the number of babies given the names of all other presidents
# during this same time period.
# 
# If the name William became more popular than the other presidential names during than before the
# presidency of Bill Clinton, then this is evidence in favor of our hypothesis.

# List the presidential first names without duplicates
first_names = prez_data['first_name'].unique()

# Query to count the number of births for a given name
# (or names) on a period between two years (inclusive)
query = '''SELECT SUM(births)
             FROM state_data
            WHERE name {}
              AND year BETWEEN {} AND {}'''

# Iterate through the presidential first names
for i, name in prez_data['first_name'].iteritems():
    
    # Identify the president's start year, end year, and tenure
    year_start = prez_data.ix[i, 'took_office_year']
    year_end = prez_data.ix[i, 'left_office_year']
    tenure = prez_data.ix[i, 'tenure']
    
    # Write the SQL code to limit data pulls to specific names
    prez_name = '= "{}"'.format(name)
    other_names = first_names[first_names != name]
    other_names = 'IN ({})'.format('"{}"'.format('", "'.join(other_names)))
    
    # Write the SQL code to pull the 4 numbers required to test the hypothesis
    prez_pre = query.format(prez_name, year_start - tenure, year_start - 1)
    other_pre = query.format(other_names, year_start - tenure, year_start - 1)
    prez_during = query.format(prez_name, year_start, year_end)
    other_during = query.format(other_names, year_start, year_end)
    
    # Compute the ratio of the number of babies born with the president's name
    # to the number of babies born with the names of other presidents before
    # the president's administration
    pre_ratio = fetch_one(prez_pre) / fetch_one(other_pre)
    
    # Compute the ratio of the number of babies born with the president's name
    # to the number of babies born with the names of other presidents during
    # the president's administration
    during_ratio = fetch_one(prez_during) / fetch_one(other_during)
    
    # Compute the difference between these two ratios
    prez_data.loc[i, 'effect'] = during_ratio - pre_ratio

# Test the hypothesis that the mean difference between the two ratios is significantly different from zero.

# Compute the t-statistic and p-value
t, p = ss.ttest_1samp(prez_data['effect'], 0)
print t
print p
