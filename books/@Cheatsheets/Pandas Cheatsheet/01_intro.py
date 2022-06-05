# -*- coding: utf-8 -*-
"""
Created on Sun Jan 16 07:21:27 2022

@author: sarak
"""

import pandas as pd
#%%
# Use the read_csv function to read in the movie dataset, and display the first five rows with the head method:
    
df = pd.read_csv('data/movie.csv')
print(df.head())

#    color      director_name  ...  aspect_ratio  movie_facebook_likes
# 0  Color      James Cameron  ...          1.78                 33000
# 1  Color     Gore Verbinski  ...          2.35                     0
# 2  Color         Sam Mendes  ...          2.35                 85000
# 3  Color  Christopher Nolan  ...          2.35                164000
# 4    NaN        Doug Walker  ...           NaN                     0
# [5 rows x 28 columns]

#%%
# index, columns, and data can be accessed directly from a DataFrame. 
# Each of these components is itself a Python object with its own unique attributes and methods. 

# Accessing the main DataFrame components
     # Extracts the index, columns, and the data of the DataFrame into separate variables, 
     # and then shows how the columns and index are inherited from the same object.

index = df.index
columns = df.columns
data = df.values


print(index)
        # RangeIndex(start=0, stop=4916, step=1)

print(columns)
        # Index(['color', 'director_name', 'num_critic_for_reviews', 'duration',
        #        'director_facebook_likes', 'actor_3_facebook_likes', 'actor_2_name',
        #        'actor_1_facebook_likes', 'gross', 'genres', 'actor_1_name',
        #        'movie_title', 'num_voted_users', 'cast_total_facebook_likes',
        #        'actor_3_name', 'facenumber_in_poster', 'plot_keywords',
        #        'movie_imdb_link', 'num_user_for_reviews', 'language', 'country',
        #        'content_rating', 'budget', 'title_year', 'actor_2_facebook_likes',
        #        'imdb_score', 'aspect_ratio', 'movie_facebook_likes'],
        #       dtype='object')


print(data)
        # [['Color' 'James Cameron' 723.0 ... 7.9 1.78 33000]
        #  ['Color' 'Gore Verbinski' 302.0 ... 7.1 2.35 0]
        #  ['Color' 'Sam Mendes' 602.0 ... 6.8 2.35 85000]
        #  ...
        #  ['Color' 'Benjamin Roberds' 13.0 ... 6.3 nan 16]
        #  ['Color' 'Daniel Hsia' 14.0 ... 6.3 2.35 660]
        #  ['Color' 'Jon Gunn' 43.0 ... 6.6 1.85 456]]
    
    
print(type(index))
        # <class 'pandas.core.indexes.range.RangeIndex'>

print(type(columns))
        # <class 'pandas.core.indexes.base.Index'>

print(type(data))
        # <class 'numpy.ndarray'>
        
# The index and the columns have the same type. The issubclass method checks whether RangeIndex is indeed a subclass of Index:
    
print(issubclass(pd.RangeIndex, pd.Index))
        # True

print(index.values)
        # [   0    1    2 ... 4913 4914 4915]
print(columns.values)
        # ['color' 'director_name' 'num_critic_for_reviews' 'duration'
        #  'director_facebook_likes' 'actor_3_facebook_likes' 'actor_2_name'
        #  'actor_1_facebook_likes' 'gross' 'genres' 'actor_1_name' 'movie_title'
        #  'num_voted_users' 'cast_total_facebook_likes' 'actor_3_name'
        #  'facenumber_in_poster' 'plot_keywords' 'movie_imdb_link'
        #  'num_user_for_reviews' 'language' 'country' 'content_rating' 'budget'
        #  'title_year' 'actor_2_facebook_likes' 'imdb_score' 'aspect_ratio'
        #  'movie_facebook_likes']

#%% Understanding data types

# Boolean: np.bool --> bool, Stored as a single byte.

# Integer: np.int  --> int, Defaulted to 64 bits. Unsigned ints are also available - np.uint.
# Float np.float  --> float Defaulted to 64 bits.

# Complex: np.complex  --> complex, Rarely seen in data analysis.

# Object: np.object O, object  --> Typically strings but is a catchall for columns with multiple different types or other Python objects (tuples, lists, dicts, and so on).

# Datetime: np.datetime64, pd.Timestamp  --> datetime64, Specific moment in time with nanosecond precision.

# Timedelta np.timedelta64, pd.Timedelta   --> timedelta64, An amount of time, from days to nanoseconds.

# Categorical pd.Categorical  --> category, Specific only to pandas. Useful for object columns with relatively few unique values.


print(df.dtypes)
        # color                         object
        # director_name                 object
        # num_critic_for_reviews       float64
        # duration                     float64
        # director_facebook_likes      float64
        # actor_3_facebook_likes       float64
        # actor_2_name                  object
        # actor_1_facebook_likes       float64
        # gross                        float64
        # genres                        object
        # actor_1_name                  object
        # movie_title                   object
        # num_voted_users                int64
        # cast_total_facebook_likes      int64
        # actor_3_name                  object
        # facenumber_in_poster         float64
        # plot_keywords                 object
        # movie_imdb_link               object
        # num_user_for_reviews         float64
        # language                      object
        # country                       object
        # content_rating                object
        # budget                       float64
        # title_year                   float64
        # actor_2_facebook_likes       float64
        # imdb_score                   float64
        # aspect_ratio                 float64
        # movie_facebook_likes           int64
        # dtype: object
print(df.dtypes.value_counts())
        # float64    13
        # object     12
        # int64       3
        # dtype: int64

# Homogeneous data is another term for referring to columns that all have the same type. 
# DataFrames as a whole may contain heterogeneous data of different data types for different columns.

#%% Selecting a single column of data as a Series

# A Series is a single column of data from a DataFrame. It is a single dimension of data, composed of just an index and the data.

# 1. Pass a column name as a string to the indexing operator to select a Series of data:

ser1 = df['director_name']
print(ser1)
        # 0           James Cameron
        # 1          Gore Verbinski
        # 2              Sam Mendes
        # 3       Christopher Nolan
        # 4             Doug Walker
               
        # 4911          Scott Smith
        # 4912                  NaN
        # 4913     Benjamin Roberds
        # 4914          Daniel Hsia
        # 4915             Jon Gunn
        # Name: director_name, Length: 4916, dtype: object
print(type(ser1))
        # <class 'pandas.core.series.Series'>

##################################################################

# 2. Alternatively, you may use the dot notation to accomplish the same task:
ser2 = df.director_name

print(ser2)
        # 0           James Cameron
        # 1          Gore Verbinski
        # 2              Sam Mendes
        # 3       Christopher Nolan
        # 4             Doug Walker
               
        # 4911          Scott Smith
        # 4912                  NaN
        # 4913     Benjamin Roberds
        # 4914          Daniel Hsia
        # 4915             Jon Gunn
        # Name: director_name, Length: 4916, dtype: object
print(type(ser2))
        # <class 'pandas.core.series.Series'>


# Passing a single string to the DataFrame indexing operator returns a Series.

##################################################################

# It is possible to turn this Series into a one-column DataFrame with the to_frame method.
# This method will use the Series name as the new column name:

director_series = df['director_name']
print(director_series.name)
        # director_name

director_frame = director_series.to_frame()
print(director_frame)
        #           director_name
        # 0         James Cameron
        # 1        Gore Verbinski
        # 2            Sam Mendes
        # 3     Christopher Nolan
        # 4           Doug Walker
        #                 ...
        # 4911        Scott Smith
        # 4912                NaN
        # 4913   Benjamin Roberds
        # 4914        Daniel Hsia
        # 4915           Jon Gunn
        
        # [4916 rows x 1 columns]
print(type(director_frame))
        # <class 'pandas.core.frame.DataFrame'>
#%% Calling Series methods
# Utilizing the single-dimensional Series is an integral part of all data analysis with pandas.

series_director_name = df['director_name']
series_actor_1_facebook_likes = df['actor_1_facebook_likes'] 


print(series_director_name.head())
        # 0        James Cameron
        # 1       Gore Verbinski
        # 2           Sam Mendes
        # 3    Christopher Nolan
        # 4          Doug Walker
        # Name: director_name, dtype: object
print(series_actor_1_facebook_likes.head())
        # 0     1000.0
        # 1    40000.0
        # 2    11000.0
        # 3    27000.0
        # 4      131.0
        # Name: actor_1_facebook_likes, dtype: float64


print(series_director_name.value_counts())
        # Steven Spielberg    26
        # Woody Allen         22
        # Martin Scorsese     20
        # Clint Eastwood      20
        # Ridley Scott        16
        #                     ..
        # John Putch           1
        # Luca Guadagnino      1
        # Sam Fell             1
        # Dan Fogelman         1
        # Daniel Hsia          1
        # Name: director_name, Length: 2397, dtype: int64
print(series_actor_1_facebook_likes.value_counts())
        # 1000.0     436
        # 11000.0    206
        # 2000.0     189
        # 3000.0     150
        # 12000.0    131
        
        # 703.0        1
        # 208.0        1
        # 79.0         1
        # 269.0        1
        # 291.0        1
        # Name: actor_1_facebook_likes, Length: 877, dtype: int64


### Counting the number of elements in the Series may be done with the size or shape parameter or the len function:
    
print(series_director_name.size)
        # 4916
print(series_director_name.shape)
        # (4916,)
print(len(series_director_name))
        # 4916
        
# count method that returns the number of non-missing values
print(series_director_name.count())
        # 4814

### Basic summary statistics
print(series_actor_1_facebook_likes.describe())

        # count      4909.000000
        # mean       6494.488491
        # std       15106.986884
        # min           0.000000
        # 25%         607.000000
        # 50%         982.000000
        # 75%       11000.000000
        # max      640000.000000
        # Name: actor_1_facebook_likes, dtype: float64

# The quantile method exists to calculate an exact quantile of numeric data:
print(series_actor_1_facebook_likes.quantile([.1, .2, .3, .4, .5, .6, .7, .8, .9]))

        # 0.1      240.0
        # 0.2      510.0
        # 0.3      694.0
        # 0.4      854.0
        # 0.5      982.0
        # 0.6     1000.0
        # 0.7     8000.0
        # 0.8    13000.0
        # 0.9    18000.0
        # Name: actor_1_facebook_likes, dtype: float64

##################################################################
# The isnull method may be used to determine whether each individual value is missing or not.
# The result will be a Series of booleans the same length as the original Series:

print(series_director_name.isnull())
print(series_actor_1_facebook_likes.isnull())
        # 0       False
        # 1       False
        # 2       False
        # 3       False
        # 4       False
         
        # 4911    False
        # 4912    False
        # 4913    False
        # 4914    False
        # 4915    False
        # Name: actor_1_facebook_likes, Length: 4916, dtype: bool


# replace all missing values within a Series with the fillna
series_actor_1_facebook_likes_filled = series_actor_1_facebook_likes.fillna(0)
print(series_actor_1_facebook_likes_filled.count())
        # 4916

# To remove the Series elements with missing values, use dropna:
series_actor_1_facebook_likes_dropped = series_actor_1_facebook_likes.dropna()
print(series_actor_1_facebook_likes_dropped.size)

        # 4909

# The result from the head method is another Series.
 
# The value_counts method produces a Series but has the unique values from the original Series as the index and the count as its values. 

# The size and count return scalar values, but shape returns a one-item tuple.

# Python treats an expression composed of only comma-separated values without parentheses as a tuple.

# The describe returns a Series with all the summary statistic names as the index and the actual statistic as the values.

# The quantile is flexible and returns a scalar value when passed a single value but returns a Series when given a list.

# The isnull, fillna, and dropna all return a Series.

##################################################################

print(series_director_name.value_counts(normalize = True))
        # Steven Spielberg    0.005401
        # Woody Allen         0.004570
        # Martin Scorsese     0.004155
        # Clint Eastwood      0.004155
        # Ridley Scott        0.003324
          
        # John Putch          0.000208
        # Luca Guadagnino     0.000208
        # Sam Fell            0.000208
        # Dan Fogelman        0.000208
        # Daniel Hsia         0.000208
        # Name: director_name, Length: 2397, dtype: float64

# The value_counts method is one of the most informative Series methods and heavily used during exploratory analysis, especially with categorical columns. 

# It defaults to returning the counts, but by setting the normalize parameter to True, the relative frequencies are returned instead, which provides another view of the distribution.



# The notnull method, which returns True for all the non-missing values:

print(series_director_name.notnull())
        # 0        True
        # 1        True
        # 2        True
        # 3        True
        # 4        True
         
        # 4911     True
        # 4912    False
        # 4913     True
        # 4914     True
        # 4915     True
        # Name: director_name, Length: 4916, dtype: bool

#%% Working with operators on a Series

# Select the imdb_score column as a Series:
series_imdb_score = df['imdb_score']
print(series_imdb_score)
        # 0       7.9
        # 1       7.1
        # 2       6.8
        # 3       8.5
        # 4       7.1
        
        # 4911    7.7
        # 4912    7.5
        # 4913    6.3
        # 4914    6.3
        # 4915    6.6
        # Name: imdb_score, Length: 4916, dtype: float64

# add one to each Series element (+, -, *, //, /)
print(series_imdb_score + 1)
        # 0       8.9
        # 1       8.1
        # 2       7.8
        # 3       9.5
        # 4       8.1
        
        # 4911    8.7
        # 4912    8.5
        # 4913    7.3
        # 4914    7.3
        # 4915    7.6
        # Name: imdb_score, Length: 4916, dtype: float64


# There exist six comparison operators, greater than (>), less than (<), greater than
# or equal to (>=), less than or equal to (<=), equal to (==), and not equal to (!=).

        # print(series_imdb_score > 7)
        # 0        True
        # 1        True
        # 2       False
        # 3        True
        # 4        True
         
        # 4911     True
        # 4912     True
        # 4913    False
        # 4914    False
        # 4915    False
        # Name: imdb_score, Length: 4916, dtype: bool
print(series_director_name == 'James Cameron')

        # 0        True
        # 1       False
        # 2       False
        # 3       False
        # 4       False
         
        # 4911    False
        # 4912    False
        # 4913    False
        # 4914    False
        # 4915    False
        # Name: director_name, Length: 4916, dtype: bool
##################################################################
series_imdb_score.add(1)                # series_imdb_score + 1
series_imdb_score.mul(2.5)              # series_imdb_score * 2.5
series_imdb_score.floordiv(7)           # series_imdb_score // 7
series_imdb_score.gt(7)                 # series_imdb_score > 7
series_imdb_score.eq('James Cameron')   # series_director_name == 'James Cameron'
##################################################################
# Operator Group
#     Arithmetic: 
#         Operator: +, -, *, /, //, %, **
#         Series method name: add, sub, mul, div, floordiv, mod, pow


#     Comparison
#         Operator: <, >, <=, >=, ==, !=
#         Series method name: lt, gt, le, ge, eq, ne
#%% Chaining Series methods together
# In Python, every variable is an object, and all objects have attributes and methods that refer to or return more objects. 
# The sequential invocation of methods using the dot notation is referred to as method chaining. 

# Pandas is a library that lends itself well to method chaining, as many Series and DataFrame methods return more Series and DataFrames, upon which more methods can be called.
# A Python version of this sentence might take the following form:
#         >>> person.drive('store')\
#         .buy('food')\
#         .drive('home')\
#         .prepare('food')\
#         .cook('food')\
#         .serve('food')\
#         .eat('food')\
#         .cleanup('dishes')

### - Chain value_counts() and head()
print(series_director_name.value_counts().head(15))
 
        # Steven Spielberg     26
        # Woody Allen          22
        # Martin Scorsese      20
        # Clint Eastwood       20
        # Ridley Scott         16
        # Spike Lee            16
        # Steven Soderbergh    15
        # Renny Harlin         15
        # Oliver Stone         14
        # Tim Burton           14
        # Barry Levinson       13
        # Joel Schumacher      13
        # Robert Zemeckis      13
        # Robert Rodriguez     13
        # Ron Howard           13
        # Name: director_name, dtype: int64

### Chain isnull() and sum()
print(series_actor_1_facebook_likes.isnull().sum())
        # 7

print(series_actor_1_facebook_likes.dtype)
        # float64

print(series_actor_1_facebook_likes.fillna(0).astype(int).head())
        # 0     1000
        # 1    40000
        # 2    11000
        # 3    27000
        # 4      131
        # Name: actor_1_facebook_likes, dtype: int32

#%% Making the index meaningful

# The index of a DataFrame provides a label for each of the rows. If no index is explicitly  provided upon DataFrame creation, then by default, a RangeIndex is created with labels as integers from 0 to n-1, where n is the number of rows.

# This recipe replaces the meaningless default row index of the movie dataset with the movie title, which is much more meaningful. A meaningful index is one that clearly identifies each row.

df_indexed = df.set_index('movie_title')
print(df_indexed)

# movie_title                                        ...                     
# Avatar                                      Color  ...                33000
# Pirates of the Caribbean: At World's End    Color  ...                    0
# Spectre                                     Color  ...                85000
# The Dark Knight Rises                       Color  ...               164000
# Star Wars: Episode VII - The Force Awakens    NaN  ...                    0
#                                           ...  ...                  ...
# Signed Sealed Delivered                     Color  ...                   84
# The Following                               Color  ...                32000
# A Plague So Pleasant                        Color  ...                   16
# Shanghai Calling                            Color  ...                  660
# My Date with Drew                           Color  ...                  456

# [4916 rows x 27 columns]

# Alternatively, it is possible to choose a column as the index upon initial read with the index_col parameter of the read_csv function:

df_indexed2 =  pd.read_csv('data/movie.csv', index_col= 'movie_title') 
##################################################################

# Conversely, it is possible to turn the index into a column with the reset_index method.
# This will make movie_title a column again and revert the index back to a RangeIndex.
# reset_index always puts the column as the very first one in the DataFrame, so the columns may not be in their original order:
df_orig = df_indexed.reset_index()

#%% Renaming row and column names

idx_rename = {'Avatar':'Ratava', 'Spectre': 'Ertceps'}
col_rename = {'director_name':'Director Name', 'num_critic_for_reviews': 'Critical Reviews'}

df_renamed = df_indexed.rename(index = idx_rename, columns = col_rename)
##################################################################
# There are multiple ways to rename row and column labels. It is possible to reassign the index and column attributes directly to a Python list. 

# This assignment works when the list has the same number of elements as the row and column labels. 

# The following code uses the tolist method on each Index object to create a Python list of labels. It then modifies a couple values in the list and reassigns the list to the attributes index and columns:

index = df_indexed.index
columns = df_indexed.columns

index_list = index.to_list()
column_list = columns.to_list()

# rename the row and column labels with list assignments
index_list[0] = 'Ratava'
index_list[2] = 'Ertceps'
column_list[1] = 'Director Name'
column_list[2] = 'Critical Reviews'

print(index_list)

print(column_list)
['color', 'Director Name', 'Critical Reviews', 'duration', 'director_facebook_likes', 'actor_3_facebook_likes', 'actor_2_name', 'actor_1_facebook_likes', 'gross', 'genres', 'actor_1_name', 'num_voted_users', 'cast_total_facebook_likes', 'actor_3_name', 'facenumber_in_poster', 'plot_keywords', 'movie_imdb_link', 'num_user_for_reviews', 'language', 'country', 'content_rating', 'budget', 'title_year', 'actor_2_facebook_likes', 'imdb_score', 'aspect_ratio', 'movie_facebook_likes']

# finally reassign the index and columns
df_indexed.index = index_list
df_indexed.columns = column_list

#%% Creating and deleting columns

# During a data analysis, it is extremely likely that you will need to create new columns to represent new variables. Commonly, these new columns will be created from previous columns already in the dataset. Pandas has a few different ways to add new columns to a DataFrame.

# The simplest way to create a new column is to assign it a scalar value. Place the name of the new column as a string into the indexing operator. Let's create the has_seen column in the movie dataset to indicate whether or not we have seen the movie. We will assign zero for every value. By default, new columns are appended to the end:

df['has_seen'] = 0

# There are several columns that contain data on the number of Facebook likes.
# Let's add up all the actor and director Facebook likes and assign them to the actor_director_facebook_likes column:

df['actor_director_facebook_likes'] = (df['actor_1_facebook_likes'] +
                                       df['actor_2_facebook_likes'] +
                                       df['actor_3_facebook_likes'] +
                                       df['director_facebook_likes'])

##################################################################

# When numeric columns are added to one another as in the preceding step, pandas defaults missing values to zero. 
# But, if all values for a particular row are missing, then pandas keeps the total as missing as well. 
# Let's check if there are missing values in our new column and fill them with 0:

df['actor_director_facebook_likes'].isnull().sum()
        # 122
df['actor_director_facebook_likes'] = df['actor_director_facebook_likes'].fillna(0)
##################################################################
# There is another column in the dataset named cast_total_facebook_likes. 
# It would be interesting to see what percentage of this column comes from our newly created column, actor_director_facebook_likes. 

# Before we create our percentage column, let's do some basic data validation. 
# Let's ensure that cast_total_facebook_likes is greater than or equal to actor_director_facebook_likes:

df['is_cast_likes_more'] = (df['cast_total_facebook_likes'] >=
                            df['actor_director_facebook_likes'])
##################################################################

# is_cast_likes_more is now a column of boolean values. 
# We can check whether all the values of this column are True with the all Series method:
df['is_cast_likes_more'].all()
#       False

##################################################################
# It turns out that there is at least one movie with more actor_director_facebook_likes than cast_total_facebook_likes. 
# It could be that director Facebook likes are not part of the cast total likes. 
# Let's backtrack and delete column actor_director_facebook_likes:

df = df.drop('actor_director_facebook_likes', axis='columns')

# Let's recreate a column of just the total actor likes:
df['actor_total_facebook_likes'] = (df['actor_1_facebook_likes'] +
                                    df['actor_2_facebook_likes'] +
                                    df['actor_3_facebook_likes'])

df['actor_total_facebook_likes'] = df['actor_total_facebook_likes'].fillna(0)
##################################################################
# Check again whether all the values in cast_total_facebook_likes are greater than the actor_total_facebook_likes:

df['is_cast_likes_more'] = (df['cast_total_facebook_likes'] >=
                            df['actor_total_facebook_likes'])

df['is_cast_likes_more'].all()
#       Truee
##################################################################
# Finally, let's calculate the percentage of the cast_total_facebook_likes that come from actor_total_facebook_likes:
df['pct_actor_cast_like'] = (df['actor_total_facebook_likes'] /
                             df['cast_total_facebook_likes'])
##################################################################
# 10. Let's validate that the min and max of this column fall between 0 and 1:
(df['pct_actor_cast_like'].min(), df['pct_actor_cast_like'].max())
        # (0.0, 1.0)
##################################################################
# We can then output this column as a Series. First, we need to set the index to the movie title so we can properly identify each value.

df.set_index('movie_title')['pct_actor_cast_like'].head()
        # movie_title
        # Avatar 0.577369
        # Pirates of the Caribbean: At World's End 0.951396
        # Spectre 0.987521
        # The Dark Knight Rises 0.683783
        # Star Wars: Episode VII - The Force Awakens 0.000000
        # Name: pct_actor_cast_like, dtype: float64
##################################################################
# It is possible to insert a new column into a specific place in a DataFrame besides the end
# with the insert method. The insert method takes the integer position of the new column
# as its first argument, the name of the new column as its second, and the values as its third.
# You will need to use the get_loc Index method to find the integer location of the column name.

# The insert method modifies the calling DataFrame in-place, so there won't be an assignment statement. The profit of each movie may be calculated by subtracting budget from gross and inserting it directly after gross with the following:
profit_index = df.columns.get_loc('gross') + 1
profit_index
        # 9
df.insert(loc=profit_index, column='profit', value = df['gross'] - df['budget'])
##################################################################
# An alternative to deleting columns with the drop method is to use the del statement:
del df['actor_director_facebook_likes']