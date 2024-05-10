import pandas as pd


def read_excel_to_dataframe(file_path):
    # Read all sheets of the Excel file
    dfs = pd.read_excel(file_path, sheet_name=None)
    # Return the dictionary of dataframes
    return dfs


# Use the function
dfs = read_excel_to_dataframe('Discovery Tour - Shadowing Days - Shadowers & Hosts - 2 .xlsx')

# Assign each dataframe to a separate variable
df1 = dfs['Shadowers']
df2 = dfs['Hosts']
df3 = dfs['areas']

# Print the dataframes
print(df1)
print(df2)
print(df3)
