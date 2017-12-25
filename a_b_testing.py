"""
   sample data analytics functions with pandas & matplotlib

   Marketing analysis for ad clicks by utm, campaign A vs. B
   Shawn Chen
"""


import pandas as pd
from matplotlib import pyplot as plt

ad_clicks = pd.read_csv('ad_clicks.csv')

# .1 view objects in file
print ad_clicks.head()

# .2 views by utm source
ad_clicks_by_utm = ad_clicks.groupby('utm_source').user_id.count().reset_index()

# .3 check if ad click occurred
ad_clicks['is_click'] = ~ad_clicks.ad_click_timestamp.isnull()
print ad_clicks

# .4 check count of ad clicks (True+False) by utm
clicks_by_source = ad_clicks.groupby(['utm_source', 'is_click']).user_id.count().reset_index()

# .5 create pivot table
clicks_pivot = clicks_by_source.pivot(
	columns = 'is_click',
	index = 'utm_source',
	values = 'user_id').reset_index()

# .6 add percent_clicked column to pivot
clicks_pivot['percent_clicked'] = clicks_pivot[True] / (clicks_pivot[True] + clicks_pivot[False])

print clicks_pivot

# .7 count experimental group (A vs. B)
ad_shown = ad_clicks.groupby('experimental_group').user_id.count().reset_index()

print ad_shown

# .8 check percentage between experimental group (A/B) & clicked ad
a_or_b_percent = ad_clicks.groupby(['experimental_group', 'is_click']).user_id.count().reset_index()

print a_or_b_percent

# .9 dataframes for a_clicks & b_clicks
a_clicks = ad_clicks[ad_clicks.experimental_group == 'A'].reset_index()
b_clicks = ad_clicks[ad_clicks.experimental_group == 'B'].reset_index()

# .10 calculate percent of users that click ad A vs B by day of the week
ad_a_clicked_by_day = a_clicks.groupby(['day', 'is_click']).user_id.count().reset_index()
ad_b_clicked_by_day = b_clicks.groupby(['day', 'is_click']).user_id.count().reset_index()

ad_a_by_day_pivot = ad_a_clicked_by_day.pivot(
    columns = 'is_click',
    index = 'day',
    values = 'user_id').reset_index()

ad_b_by_day_pivot = ad_b_clicked_by_day.pivot(
    columns = 'is_click',
    index = 'day',
    values = 'user_id').reset_index()

# derive % of ad clicks by day of week (per each ad type - A vs. B)
ad_a_by_day_pivot['percent_clicked'] = ad_a_by_day_pivot[True] / (ad_a_by_day_pivot[True] + ad_a_by_day_pivot[False])
ad_b_by_day_pivot['percent_clicked'] = ad_b_by_day_pivot[True] / (ad_b_by_day_pivot[True] + ad_b_by_day_pivot[False])

print ad_a_by_day_pivot
print ad_b_by_day_pivot

# create visuals for project
plt.figure(figsize=(14, 8))
ax = plt.subplot()

y_values1 = ad_a_by_day_pivot['percent_clicked']
y_values2 = ad_b_by_day_pivot['percent_clicked']

plt.ylim(0, 0.50)
plt.xlim(0, 14.5)

# sales set 1
n = 1  # This is our first dataset (out of 2)
t = 2 # Number of datasets
d = 7 # Number of sets of bars
w = 0.8 # Width of each bar
ad_a_x = [t*(element) + w*n for element in range(d)]

# sales set 2
n = 2  # This is our first dataset (out of 2)
t = 2 # Number of datasets
d = 7 # Number of sets of bars
w = 0.8 # Width of each bar
ad_b_x = [t*(element) + w*n for element in range(d)]

plt.bar(ad_a_x, y_values1, label='ad A clicks')
plt.bar(ad_b_x, y_values2, label='ad B clicks')

plt.xlabel('Day of the Week')
plt.ylabel('Percentage clicked (ad) in decimal')

plt.title('Compare ads A vs. B clicked percentage')

middle_x = [(a + b) / 2.0 for a,b in zip(ad_a_x, ad_b_x)]

ax.set_xticks(middle_x)
ax.set_xticklabels(ad_a_by_day_pivot['day'])

plt.legend()

plt.show()
