# convert a df column into a numpy array (.iloc and .values)
column_data= df.iloc[:, :].values     # the dataframe has only one column
column_data
###########################################################################
pd.set_option('max_colwidth', -1)
pd.set_option('display.width', 1000)
pd.set_option('display.max_rows', 1000)
pd.set_option('display.max_columns', 1000)
