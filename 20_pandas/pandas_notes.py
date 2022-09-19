# list all of the sheets of a excel file

excel_df = pd.ExcelFile(data_path)
excel_df.sheet_names  # all sheet names
