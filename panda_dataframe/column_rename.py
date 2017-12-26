import pandas as pd

df = pd.read_csv('imdb.csv')


# rename columns in bulk - must define all
df.columns = ['ID', 'Title', 'Category', 'Year Released', 'Rating']

# selective rename of column, 'inplace=True' will overwrite instead of creating new dataframe
df.rename(columns={
  'name': 'movie_title'},
          inplace=True)

print df