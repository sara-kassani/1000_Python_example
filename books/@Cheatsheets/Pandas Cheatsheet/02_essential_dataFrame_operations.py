# -*- coding: utf-8 -*-
"""
Created on Sun Jan 16 13:02:35 2022

@author: sarak
"""

import pandas as pd

#%% Selecting multiple DataFrame columns
df = pd.read_csv('data/movie.csv')

df_actor_director = df[['actor_1_name', 'actor_2_name','actor_3_name', 'director_name']]
print(df_actor_director.head())
#       actor_1_name      actor_2_name          actor_3_name      director_name
# 0      CCH Pounder  Joel David Moore             Wes Studi      James Cameron
# 1      Johnny Depp     Orlando Bloom        Jack Davenport     Gore Verbinski
# 2  Christoph Waltz      Rory Kinnear      Stephanie Sigman         Sam Mendes
# 3        Tom Hardy    Christian Bale  Joseph Gordon-Levitt  Christopher Nolan
# 4      Doug Walker        Rob Walker                   NaN        Doug Walker


# Alternative method:
cols = ['actor_1_name', 'actor_2_name', 'actor_3_name', 'director_name']
df_actor_director = df[cols]

# DataFrame indexing:  If a string is passed, it will return a single-dimensional Series. 
# If a list is passed to the indexing operator, it returns a DataFrame of all the columns in the list in the specified order

#####################################################################
# Select a single column as a DataFrame rather than as a Series
df_director = df[['director_name']]
print(df_director.head())
        #        director_name
        # 0      James Cameron
        # 1     Gore Verbinski
        # 2         Sam Mendes
        # 3  Christopher Nolan
        # 4        Doug Walker
print(type(df_director))
        # <class 'pandas.core.frame.DataFrame'>
#####################################################################
# Selecting columns with methods

# Select only the integer columns
df.select_dtypes(include=['int']).head()
#########
# Select all the numeric columns
df.select_dtypes(include=['number']).head()
#########
# Search column names (or index labels) based on which parameter is used. Here, we use the like parameter to search for all column names that contain the exact string, facebook:
df.filter(like='facebook').head()
#########
# The filter method allows columns to be searched through regular expressions with the regex parameter. Here, we search for all columns that have a digit somewhere in their name:
df.filter(regex='\d').head()

#####################################################################
# Regular expressions are character sequences that represent search patterns to be used to select different parts of the text. They allow for very complex and highly specific pattern matching.
#####################################################################
#%% Ordering column names sensibly

print(df.columns)

disc_core = ['movie_title', 'title_year', 'content_rating', 'genres']
disc_people = ['director_name', 'actor_1_name', 'actor_2_name', 'actor_3_name']
disc_other = ['color', 'country', 'language', 'plot_keywords', 'movie_imdb_link']
cont_fb = ['director_facebook_likes', 'actor_1_facebook_likes',
           'actor_2_facebook_likes', 'actor_3_facebook_likes',
           'cast_total_facebook_likes', 'movie_facebook_likes']
cont_finance = ['budget', 'gross']
cont_num_reviews = ['num_voted_users', 'num_user_for_reviews', 'num_critic_for_reviews']
cont_other = ['imdb_score', 'duration', 'aspect_ratio', 'facenumber_in_poster']

new_col_order = disc_core + disc_people + disc_other + cont_fb + cont_finance + cont_num_reviews + cont_other
set(df.columns) == set(new_col_order)

df2 = df[new_col_order]

print(df2.head())

#%% Chaining DataFrame methods together

print(df.isnull().sum().head())
        # color                       19
        # director_name              102
        # num_critic_for_reviews      49
        # duration                    15
        # director_facebook_likes    102
        # dtype: int64
print(df.isnull().sum().sum())
        # 2654

print(df.isnull().any().any()) # whether there are any missing values in the DataFrame
        # True
        
df.select_dtypes(['object']).fillna('').min()
df.select_dtypes(['object']).fillna('').min()

#%% Transposing the direction of a DataFrame operation

print(df[['movie_facebook_likes']].sum(axis = 'index'))
print(df[['movie_facebook_likes']].sum(axis = 'columns'))

# The cumsum method with axis=1 accumulates the race percentages across each row.
print(df[['movie_facebook_likes']].cumsum(axis = 1))
#####################################################################
print(df.isnull().sum(axis = 1).sort_values(ascending = True).head())
#####################################################################
df = df.dropna(how = 'all')
print(df.isnull().sum())

print(df[['movie_facebook_likes']].ge(1015).sum(axis = 'columns'))
