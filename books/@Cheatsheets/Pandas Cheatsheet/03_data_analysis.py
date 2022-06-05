# -*- coding: utf-8 -*-
"""
Created on Sun Jan 16 14:03:00 2022

@author: sarak
"""
import pandas as pd
import numpy as np

df = pd.read_csv('data/college.csv')
print(df.head())
print(df.columns)
# Index(['INSTNM', 'CITY', 'STABBR', 'HBCU', 'MENONLY', 'WOMENONLY', 'RELAFFIL',
#        'SATVRMID', 'SATMTMID', 'DISTANCEONLY', 'UGDS', 'UGDS_WHITE',
#        'UGDS_BLACK', 'UGDS_HISP', 'UGDS_ASIAN', 'UGDS_AIAN', 'UGDS_NHPI',
#        'UGDS_2MOR', 'UGDS_NRA', 'UGDS_UNKN', 'PPTUG_EF', 'CURROPER', 'PCTPELL',
#        'PCTFLOAN', 'UG25ABV', 'MD_EARN_WNE_P10', 'GRAD_DEBT_MDN_SUPP'],
#       dtype='object')

print(df.shape)
        # (7535, 27)
print('***' * 15)
print(df.info())
        # <class 'pandas.core.frame.DataFrame'>
        # RangeIndex: 7535 entries, 0 to 7534
        # Data columns (total 27 columns):
        #  #   Column              Non-Null Count  Dtype  
        # ---  ------              --------------  -----  
        #  0   INSTNM              7535 non-null   object 
        #  1   CITY                7535 non-null   object 
        #  2   STABBR              7535 non-null   object 
        #  3   HBCU                7164 non-null   float64
        #  4   MENONLY             7164 non-null   float64
        #  5   WOMENONLY           7164 non-null   float64
        #  6   RELAFFIL            7535 non-null   int64  
        #  7   SATVRMID            1185 non-null   float64
        #  8   SATMTMID            1196 non-null   float64
        #  9   DISTANCEONLY        7164 non-null   float64
        #  10  UGDS                6874 non-null   float64
        #  11  UGDS_WHITE          6874 non-null   float64
        #  12  UGDS_BLACK          6874 non-null   float64
        #  13  UGDS_HISP           6874 non-null   float64
        #  14  UGDS_ASIAN          6874 non-null   float64
        #  15  UGDS_AIAN           6874 non-null   float64
        #  16  UGDS_NHPI           6874 non-null   float64
        #  17  UGDS_2MOR           6874 non-null   float64
        #  18  UGDS_NRA            6874 non-null   float64
        #  19  UGDS_UNKN           6874 non-null   float64
        #  20  PPTUG_EF            6853 non-null   float64
        #  21  CURROPER            7535 non-null   int64  
        #  22  PCTPELL             6849 non-null   float64
        #  23  PCTFLOAN            6849 non-null   float64
        #  24  UG25ABV             6718 non-null   float64
        #  25  MD_EARN_WNE_P10     6413 non-null   object 
        #  26  GRAD_DEBT_MDN_SUPP  7503 non-null   object 
        # dtypes: float64(20), int64(2), object(5)
        # memory usage: 1.6+ MB
        # None


# Get summary statistics for the numerical columns and transpose the DataFrame for more readable output:        
print(df.describe(include= np.number).T)
        #                count         mean  ...          75%          max
        # HBCU          7164.0     0.014238  ...     0.000000       1.0000
        # MENONLY       7164.0     0.009213  ...     0.000000       1.0000
        # WOMENONLY     7164.0     0.005304  ...     0.000000       1.0000
        # RELAFFIL      7535.0     0.190975  ...     0.000000       1.0000
        # SATVRMID      1185.0   522.819409  ...   555.000000     765.0000
        # SATMTMID      1196.0   530.765050  ...   565.000000     785.0000
        # DISTANCEONLY  7164.0     0.005583  ...     0.000000       1.0000
        # UGDS          6874.0  2356.837940  ...  1929.500000  151558.0000
        # UGDS_WHITE    6874.0     0.510207  ...     0.747875       1.0000
        # UGDS_BLACK    6874.0     0.189997  ...     0.257700       1.0000
        # UGDS_HISP     6874.0     0.161635  ...     0.198875       1.0000
        # UGDS_ASIAN    6874.0     0.033544  ...     0.032700       0.9727
        # UGDS_AIAN     6874.0     0.013813  ...     0.007300       1.0000
        # UGDS_NHPI     6874.0     0.004569  ...     0.002500       0.9983
        # UGDS_2MOR     6874.0     0.023950  ...     0.033900       0.5333
        # UGDS_NRA      6874.0     0.016086  ...     0.011700       0.9286
        # UGDS_UNKN     6874.0     0.045181  ...     0.045400       0.9027
        # PPTUG_EF      6853.0     0.226639  ...     0.376900       1.0000
        # CURROPER      7535.0     0.923291  ...     1.000000       1.0000
        # PCTPELL       6849.0     0.530643  ...     0.712900       1.0000
        # PCTFLOAN      6849.0     0.522211  ...     0.745000       1.0000
        # UG25ABV       6718.0     0.410021  ...     0.572275       1.0000
        
        # [22 rows x 8 columns]

# Get summary statistics for the object and categorical columns:
print(df.describe(include= [object, pd.Categorical]).T)

        #                    count unique                       top  freq
        # INSTNM              7535   7535  Alabama A & M University     1
        # CITY                7535   2514                  New York    87
        # STABBR              7535     59                        CA   773
        # MD_EARN_WNE_P10     6413    598         PrivacySuppressed   822
        # GRAD_DEBT_MDN_SUPP  7503   2038         PrivacySuppressed  1510

print(df.describe(include=[np.number], percentiles= [.01, .05, .10, .25, .5,.75, .9, .95, .99]).T)

        #                count         mean  ...           99%          max
        # HBCU          7164.0     0.014238  ...      1.000000       1.0000
        # MENONLY       7164.0     0.009213  ...      0.000000       1.0000
        # WOMENONLY     7164.0     0.005304  ...      0.000000       1.0000
        # RELAFFIL      7535.0     0.190975  ...      1.000000       1.0000
        # SATVRMID      1185.0   522.819409  ...    730.000000     765.0000
        # SATMTMID      1196.0   530.765050  ...    745.250000     785.0000
        # DISTANCEONLY  7164.0     0.005583  ...      0.000000       1.0000
        # UGDS          6874.0  2356.837940  ...  26015.290000  151558.0000
        # UGDS_WHITE    6874.0     0.510207  ...      1.000000       1.0000
        # UGDS_BLACK    6874.0     0.189997  ...      0.961467       1.0000
        # UGDS_HISP     6874.0     0.161635  ...      1.000000       1.0000
        # UGDS_ASIAN    6874.0     0.033544  ...      0.346429       0.9727
        # UGDS_AIAN     6874.0     0.013813  ...      0.209326       1.0000
        # UGDS_NHPI     6874.0     0.004569  ...      0.050508       0.9983
        # UGDS_2MOR     6874.0     0.023950  ...      0.133154       0.5333
        # UGDS_NRA      6874.0     0.016086  ...      0.236989       0.9286
        # UGDS_UNKN     6874.0     0.045181  ...      0.496581       0.9027
        # PPTUG_EF      6853.0     0.226639  ...      0.946724       1.0000
        # CURROPER      7535.0     0.923291  ...      1.000000       1.0000
        # PCTPELL       6849.0     0.530643  ...      0.993908       1.0000
        # PCTFLOAN      6849.0     0.522211  ...      0.986368       1.0000
        # UG25ABV       6718.0     0.410021  ...      0.917383       1.0000
        
        # [22 rows x 14 columns]
#%% Reducing memory by changing data types
# This recipe changes the data type of one of the object columns from the college dataset to the special pandas Categorical data type to drastically reduce its memory usage.


different_cols = ['RELAFFIL', 'SATMTMID', 'CURROPER', 'INSTNM', 'STABBR']
col2 = df.loc[:, different_cols]
print(col2.head())
        #    RELAFFIL  SATMTMID  CURROPER                               INSTNM STABBR
        # 0         0     420.0         1             Alabama A & M University     AL
        # 1         0     565.0         1  University of Alabama at Birmingham     AL
        # 2         1       NaN         1                   Amridge University     AL
        # 3         0     590.0         1  University of Alabama in Huntsville     AL
        # 4         0     430.0         1             Alabama State University     AL
print(col2.dtypes)
        # RELAFFIL      int64
        # SATMTMID    float64
        # CURROPER      int64
        # INSTNM       object
        # STABBR       object
        # dtype: object

# Find the memory usage of each column with the memory_usage method:
original_mem = col2.memory_usage(deep = True)
print(original_mem)
        # Index          128
        # RELAFFIL     60280
        # SATMTMID     60280
        # CURROPER     60280
        # INSTNM      660240
        # STABBR      444565
        # dtype: int64

# There is no need to use 64 bits for the RELAFFIL column as it contains only 0/1 values. 
# Let's convert this column to an 8-bit (1 byte) integer with the astype method:

col2['RELAFFIL'] = col2['RELAFFIL'].astype(np.int8)
print(col2.dtypes)

# Find the memory usage of each column again and note the large reduction:
print(df[different_cols].memory_usage(deep=True))
        # Index          128
        # RELAFFIL     60280
        # SATMTMID     60280
        # CURROPER     60280
        # INSTNM      660240
        # STABBR      444565
        # dtype: int64


# To save even more memory, you will want to consider changing object data types
# to categorical if they have a reasonably low cardinality (number of unique values). 
# Let's first check the number of unique values for both the object columns:
print(col2.select_dtypes(include=['object']).nunique())

col2['STABBR'] = col2['STABBR'].astype('category')
print(col2.dtypes)

new_mem = col2.memory_usage(deep=True)
print(new_mem)

print(new_mem / original_mem)

        # Index       1.000000
        # RELAFFIL    0.125000
        # SATMTMID    1.000000
        # CURROPER    1.000000
        # INSTNM      1.000695
        # STABBR      0.029512
        # dtype: float64
# The memory units displayed are in bytes and not bits. One byte is
# equivalent to 8 bits, so when RELAFFIL was changed to an 8-bit integer, it
# uses one 1 byte of memory and as there are 7,535 rows, its memory
# footprint is equivalent to 7,535 bytes.

#%% Selecting the smallest of the largest
df_movie = pd.read_csv('data/movie.csv')
df_movie2 = df_movie[['movie_title', 'imdb_score', 'budget']]
print(df_movie2.head())

# Use the nlargest method to select the top 100 movies by imdb_score:
print(df_movie2.nlargest(100, 'imdb_score'))

# Chain the nsmallest method to return the five lowest budget films among those with a top 100 score:
print(df_movie2.nlargest(100, 'imdb_score').nsmallest(5, 'budget'))


#%% Selecting the largest of each group by sorting
df_movie3 = df_movie[['movie_title', 'title_year', 'imdb_score']]

# Use the sort_values method to sort the DataFrame by title_year. The default behavior sorts from the smallest to largest. 
# Use the ascending parameter to invert this behavior by setting it equal to True:

df_movie3.sort_values('title_year', ascending = True).head()
        #                movie_title  imdb_score    budget
        # 4804        Butterfly Girl         8.7  180000.0
        # 4801    Children of Heaven         8.5  180000.0
        # 4706          12 Angry Men         8.9  350000.0
        # 4550          A Separation         8.4  500000.0
        # 4636  The Other Dream Team         8.4  500000.0
df_movie4 = df_movie3.sort_values(['title_year', 'imdb_score'], ascending = False)
print(type(df_movie4))

        # 4804        Butterfly Girl         8.7  180000.0
        # 4801    Children of Heaven         8.5  180000.0
        # 4706          12 Angry Men         8.9  350000.0
        # 4550          A Separation         8.4  500000.0
        # 4636  The Other Dream Team         8.4  500000.0
        # <class 'pandas.core.frame.DataFrame'>
        
        
# Now, we use the drop_duplicates method to keep only the first row of every year:
movie_top_year = df_movie4.drop_duplicates(subset='title_year')
print(movie_top_year.head())

        #                                   movie_title  title_year  imdb_score
        # 4312                     Kickboxer: Vengeance      2016.0         9.1
        # 3745                          Running Forever      2015.0         8.6
        # 4369                   Queen of the Mountains      2014.0         8.7
        # 3935  Batman: The Dark Knight Returns, Part 2      2013.0         8.4
        # 3                       The Dark Knight Rises      2012.0         8.5


df_movie5 = df_movie[['movie_title', 'title_year', 'content_rating', 'budget']]
df_movie5_sorted = df_movie5.sort_values(['title_year', 'content_rating', 'budget'], 
                                      ascending=[False, False, True])
df_result = df_movie5_sorted.drop_duplicates(subset=['title_year', 'content_rating']).head(10)
print(df_result)
        #                                   movie_title  title_year  imdb_score
        # 4312                     Kickboxer: Vengeance      2016.0         9.1
        # 3745                          Running Forever      2015.0         8.6
        # 4369                   Queen of the Mountains      2014.0         8.7
        # 3935  Batman: The Dark Knight Returns, Part 2      2013.0         8.4
        # 3                       The Dark Knight Rises      2012.0         8.5
        #                                           movie_title  ...     budget
        # 4026                                        Compadres  ...  3000000.0
        # 4658                              Fight to the Finish  ...   150000.0
        # 4661                                       Rodeo Girl  ...   500000.0
        # 3252                                      The Wailing  ...        NaN
        # 4659                   Alleluia! The Devil's Carnival  ...   500000.0
        # 4731                                          Bizarre  ...   500000.0
        # 812                                  The Ridiculous 6  ...        NaN
        # 4831                                      The Gallows  ...   100000.0
        # 4825                                 Romantic Schemer  ...   125000.0
        # 3796  R.L. Stine's Monsterville: The Cabinet of Souls  ...  4400000.0
        
        # [10 rows x 4 columns]

#%% Replicating nlargest with sort_values
df_movie2 = df_movie[['movie_title', 'imdb_score', 'budget']]
movie_smallest_largest = df_movie2.nlargest(100, 'imdb_score').nsmallest(5, 'budget')
print(movie_smallest_largest)
        #                movie_title  imdb_score    budget
        # 4804        Butterfly Girl         8.7  180000.0
        # 4801    Children of Heaven         8.5  180000.0
        # 4706          12 Angry Men         8.9  350000.0
        # 4550          A Separation         8.4  500000.0
        # 4636  The Other Dream Team         8.4  500000.0

df_movie2.sort_values('imdb_score', ascending=False).head(100)
df_movie2.sort_values('imdb_score', ascending=False).head(100).sort_values('budget').head()
df_movie2.nlargest(100, 'imdb_score').tail()
df_movie2.sort_values('imdb_score', ascending=False).head(100).tail()

