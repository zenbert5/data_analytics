import pandas as pd

orders = pd.read_csv('orders.csv')

print orders.head(10)

most_expensive = orders.price.max()

# count of unique shoe colors
num_colors = orders.shoe_color.nunique()

# find the pricey shoes by max price for each shoe type
pricey_shoes = orders.groupby('shoe_type').price.max().reset_index()

# count of shoes by type and color - make dataframe with new index
shoe_counts = orders.groupby(['shoe_type', 'shoe_color']).id.count().reset_index()

shoe_counts_pivot = shoe_counts.pivot(
    columns = 'shoe_color',
	index = 'shoe_type',
	values = 'id').reset_index()


# 2nd example - visitors to website
user_visits = pd.read_csv('page_visits.csv')

print user_visits.head()

click_source = user_visits.groupby('utm_source').id.count().reset_index()

# group by reference source (search engine) and month - aggregate of count, reindexed and pivoted
click_source_by_month = user_visits.groupby(['utm_source', 'month']).id.count().reset_index()

click_source_by_month_pivot = click_source_by_month.pivot(
	columns = 'month',
	index = 'utm_source',
	values = 'id').reset_index()

print click_source_by_month_pivot

print orders

print pricey_shoes

print shoe_counts_pivot

"""
Command	Description
mean	Average of all values in column
std	    Standard deviation
median	Median
max	    Maximum value in column
min	    Minimum value in column
count	Number of values in column
nunique	Number of unique values in column
unique	List of unique values in column
"""