import pandas as pd

df = pd.read_csv('employees.csv')

# row denotes for each 'row' within the dataframe
total_earned = lambda row: (40 * row.hourly_wage) +(row.hours_worked - 40) * row.hourly_wage * 1.5 \
    if row.hours_worked > 40 else row.hourly_wage * row.hours_worked

# axis=1 creates new column
df['total_earned'] = df.apply(total_earned, axis=1)

print df