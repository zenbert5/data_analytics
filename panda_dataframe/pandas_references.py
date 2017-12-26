import pandas as pd

df = pd.DataFrame([
  ['January', 100, 100, 23, 100],
  ['February', 51, 45, 145, 45],
  ['March', 81, 96, 65, 96],
  ['April', 80, 80, 54, 180],
  ['May', 51, 54, 54, 154],
  ['June', 112, 109, 79, 129]],
  columns=['month', 'clinic_east',
           'clinic_north', 'clinic_south',
           'clinic_west']
)

# examples
# pd.read_csv ('filename') open handles for filename
# pd.head() by default reads 5 but can accept integer to take more rows

# select all data in column [3] 'clinic_north'
clinic_north = df.clinic_north
print(type(clinic_north))
print(type(df))

# conditional select if month == january
january = df[df.month == 'January']
print(january)

# select march_april data if month column matches 'March' or 'April'
march_april = df[(df.month == 'March') | (df.month == 'April')]
print (march_april)

# use 'isin' function for multi-conditional matching
january_february_march = df[df.month.isin(['January', 'February', 'March'])]
print(january_february_march)


# example - select rows based on index
df2 = df.loc[[1, 3, 5]]
print(df2)

# example - create new table (df3) based on df2 but reset index - result is new column 'index' is created with old index
df3 = df2.reset_index()
print(df3)

# example - create new table (df2) by assigning existing df2 table but drop old index, result is df2 table with new index
df2 = df2.reset_index(drop=True)
print(df2)