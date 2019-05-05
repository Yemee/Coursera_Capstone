###Question two is down here


df1 = df_toronto.sort_values('Postcode')
df1.head()

df2 = pd.read_csv("Geospatial_Coordinates.csv")
df2.head()

df_merged = pd.merge(df1, df2, left_on=['Postcode'],
              right_on=['Postal Code'],
              how='inner')
df_merged.head()

del df_merged['Postal Code']
df_merged.head()

