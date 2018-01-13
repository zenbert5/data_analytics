# This import only needs to happen once, at the beginning of the notebook
from codecademySQL import sql_query
import pandas as pd
from matplotlib import pyplot as plt
from scipy.stats import chi2_contingency

# Here's an example of a query that just displays some data
sql_query('''
SELECT *
FROM visits
LIMIT 5
''')

# Examine fitness_tests here
sql_query('''
SELECT *
FROM fitness_tests
LIMIT 5
''')

# Here's an example where we save the data to a DataFrame
sql_query('''
SELECT *
FROM applications
LIMIT 5
''')

# Examine purchases here
sql_query('''
SELECT *
FROM purchases
LIMIT 5
''')

# Create multiple join query of tables into one and assign to dataframe df
df = sql_query('''
SELECT visits.first_name, visits.last_name, visits.gender, visits.email, visits.visit_date, fitness_tests.fitness_test_date, applications.application_date, purchases.purchase_date
FROM visits
LEFT JOIN fitness_tests 
ON (visits.first_name = fitness_tests.first_name 
    AND visits.last_name = fitness_tests.last_name 
    AND visits.email = fitness_tests.email
    )
LEFT JOIN applications
ON (visits.first_name = applications.first_name
    AND visits.last_name = applications.last_name
    AND visits.email = applications.email
    )
LEFT JOIN purchases
ON (visits.first_name = purchases.first_name
    AND visits.last_name = purchases.last_name
    AND visits.email = purchases.email
    )
WHERE visits.visit_date >= '7-1-17'
''')

# print dataframe and stats
print df.head(), df.count()

# create A & B test groups
df['ab_test_group'] = df.fitness_test_date.apply(lambda x: 'A' if pd.notnull(x) else 'B')

# create subframe of A B counters (of each test group)
ab_counts = df.groupby('ab_test_group').email.count().reset_index()

# create pie chart illustrating the percentage difference
pie_halves = ["Had Fitness Test", "No Fitness Test"]
plt.pie(ab_counts.email, autopct='%.2f')
plt.axis('equal')
plt.legend(pie_halves)
plt.title('Signed up for fitness test v. did not')

plt.show()

# tabulate the applicants from each group
df['is_application'] = df.application_date.apply(lambda x: 'Application' if pd.notnull(x) else 'No Application')
app_counts = df.groupby(['ab_test_group', 'is_application']).email.count().reset_index()

# create pivot table
app_pivot = app_counts.pivot(
	columns = 'is_application',
	index = 'ab_test_group',
    values = 'email'
    ).reset_index()

# add total and percentage of success
app_pivot['Total'] = app_pivot['Application'] + app_pivot['No Application']
app_pivot['Percent'] = app_pivot['Application'] / app_pivot['Total']

print app_pivot

# calculate pval for significance
contingency = [[app_pivot['Application'][0], app_pivot['No Application'][0]],
               [app_pivot['Application'][1], app_pivot['No Application'][1]]]

# calculate pval
chi2, pval, dof, expected = chi2_contingency(contingency)

print pval

df['is_member'] = df.purchase_date.apply(lambda x: 'Member' if pd.notnull(x) else 'Not Member')

just_apps = df[(pd.notnull(df.application_date))].reset_index()

# print just_apps

member_count = just_apps.groupby(['ab_test_group', 'is_member']).email.count().reset_index()
member_pivot = member_count.pivot(
    columns = 'is_member',
    index = 'ab_test_group',
    values = 'email'
    ).reset_index()

member_pivot['Total'] = member_pivot['Member'] + member_pivot['Not Member']
member_pivot['Percent Purchase'] = member_pivot['Member'] / member_pivot['Total']

print member_pivot

contingency = [[member_pivot['Member'][0], member_pivot['Not Member'][0]],
               [member_pivot['Member'][1], member_pivot['Not Member'][1]]]

# calculate pval
chi2, m_pval, dof, expected = chi2_contingency(contingency)

print m_pval

all_visitors_purchased = df.groupby(['ab_test_group', 'is_member']).email.count().reset_index()

final_member_pivot = all_visitors_purchased.pivot(
    columns = 'is_member',
    index = 'ab_test_group',
    values = 'email'
    ).reset_index()

final_member_pivot['Total'] = final_member_pivot['Member'] + final_member_pivot['Not Member']
final_member_pivot['Percent Purchase'] = final_member_pivot['Member'] / final_member_pivot['Total']

print final_member_pivot

contingency = [[final_member_pivot['Member'][0], final_member_pivot['Not Member'][0]],
               [final_member_pivot['Member'][1], final_member_pivot['Not Member'][1]]]

# calculate significance
chi2, fm_pval, dof, expected = chi2_contingency(contingency)

print fm_pval