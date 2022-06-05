# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 08:08:44 2022

@author: sarak
"""

#%% Selecting Subsets of Data
"""
Every dimension of data in a Series or DataFrame is labeled through an Index object. It is
this Index that separates pandas data structures from NumPy's n-dimensional array.
Indexes provide meaningful labels for each row and column of data, and pandas users have
the ability to select data through the use of these labels. Additionally, pandas allows its
users to select data by the integer location of the rows and columns. This dual selection
capability, one using labels and the other using integer location, makes for powerful yet
confusing syntax to select subsets of data.

Selecting data through the use of labels or integer location is not unique to pandas. Python
dictionaries and lists are built-in data structures that select their data in exactly one of these ways. Both dictionaries and lists have precise instructions and limited use-cases for what
may be passed to the indexing operator. A dictionary's key (its label) must be an immutable
object, such as a string, integer, or tuple. Lists must either use integers or slice objects for
selection. Dictionaries can only select one object at a time by passing the key to the indexing
operator. In some sense, pandas is combining the ability to select data using integers, as
with lists, and labels, as with dictionaries.
"""
#%% Selecting Series data
"""
In addition to the indexing operator itself, the .iloc and .loc attributes are available and use the indexing operator in their own unique ways. Collectively, these attributes are called the indexers.

The indexing terminology can get confusing. The term indexing operator
is used here to distinguish it from the other indexers. It refers to the
brackets, [] directly after a Series or DataFrame. For instance, given a
Series s, you can select data in the following ways: s[item] and
s.loc[item]. The first uses the indexing operator. The second uses the
.loc indexer.

Series and DataFrame indexers allow selection by integer location (like Python lists) and by
label (like Python dictionaries). 

The .iloc indexer selects only by integer location and works similarly to Python lists.

The .loc indexer selects only by index label, which is similar to how Python dictionaries work.

"""
import numpy as np
import pandas as pd
df_college = pd.read_csv('data/college.csv', index_col= 'INSTNM')
print(df_college.shape)
        # (7535, 26)
seri_city= df_college['CITY']
print(seri_city.head(6))
            # INSTNM
            # Alabama A & M University                   Normal
            # University of Alabama at Birmingham    Birmingham
            # Amridge University                     Montgomery
            # University of Alabama in Huntsville    Huntsville
            # Alabama State University               Montgomery
            # The University of Alabama              Tuscaloosa
#######################################################################
### iloc
# The .iloc indexer makes selections only by integer location. Passing an integer
# to it returns a scalar value:
print(seri_city.iloc[3])

# To select several different integer locations, pass a list to .iloc. This returns a Series:
print(seri_city.iloc[[1,3,5,7]])
            # INSTNM
            # University of Alabama at Birmingham    Birmingham
            # University of Alabama in Huntsville    Huntsville
            # The University of Alabama              Tuscaloosa
            # Athens State University                    Athens

# To select an equally spaced partition of data, use slice notation:
print(seri_city.iloc[4:50:10])

#######################################################################
### loc
print(seri_city.loc['Heritage Christian University'])
            # Florence
# To select several disjoint labels, use a list:

np.random.seed(1)
labels = list(np.random.choice(seri_city.index, 4))
labels
            # ['Northwest HVAC/R Training Center',
            # 'California State University-Dominguez Hills',
            # 'Lower Columbia College',
            # 'Southwest Acupuncture College-Boulder']
seri_city.loc[labels]

# To select an equally spaced partition of data, use slice notation. Make sure that
# the start and stop values are strings. You can use an integer to specify the step
# size of the slice:

print(seri_city.loc['Alabama State University':
'Reid State Technical College':10])
#######################################################################
# Pass an integer to the .iloc indexer to select an entire row at that position:
print(df_college.iloc[60])

# x= df_college.iloc[60]
# print(type(x))
# print(x.shape)
#                 # <class 'pandas.core.series.Series'>
#                 # (26,)

# To get the same row as the preceding step, pass the index label to the .loc indexer:
df_college.loc['University of Alaska Anchorage']

# To select a disjointed set of rows as a DataFrame, pass a list of integers to the .iloc indexer:
df_college.iloc[[60, 99, 3]]


# The same DataFrame from step 4 may be reproduced using .loc by passing it a list of the exact institution names:

labels = ['University of Alaska Anchorage',
'International Academy of Hair Design',
'University of Alabama in Huntsville']
df_college.loc[labels]


# Use slice notation with .iloc to select an entire segment of the data:
df_college.iloc[99:102]



# Slice notation also works with the .loc indexer and is inclusive of the last label:
start = 'International Academy of Hair Design'
stop = 'Mesa Community College'
df_college.loc[start:stop]

#######################################################################

# Selecting DataFrame rows and columns simultaneously

df_college.iloc[:3, :4]
df_college.loc[:'Amridge University', :'MENONLY']


# Select all the rows of two different columns:
df_college.iloc[:, [4,6]].head()
df_college.loc[:, ['WOMENONLY', 'SATVRMID']].head()

# Select disjointed rows and columns:
df_college.iloc[[100, 200], [7, 15]]
rows = ['GateWay Community College',
'American Baptist Seminary of the West']
columns = ['SATMTMID', 'UGDS_NHPI']
df_college.loc[rows, columns]

# Select a single scalar value:
columns.iloc[5, -4]
columns.loc['The University of Alabama', 'PCTFLOAN']

# 5. Slice the rows and select a single column:
columns.iloc[90:80:-2, 5]
start = 'Empire Beauty School-Flagstaff'
stop = 'Arizona State University-Tempe'
columns.loc[start:stop:-2, 'RELAFFIL']

#######################################################################
# Selecting data with both integers and labels
# Use the Index method get_loc to find the integer position of the desired columns:
    
col_start = college.columns.get_loc('UGDS_WHITE')
col_end = college.columns.get_loc('UGDS_UNKN') + 1
col_start, col_end

# Use col_start and col_end to select columns by integer location using .iloc:
college.iloc[:5, col_start:col_end]

