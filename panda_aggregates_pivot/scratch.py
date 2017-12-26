import pandas as pd
import numpy as np

user_visits = pd.read_csv('page_visits.csv')

print user_visits.head()

click_source = user_visits.groupby('utm_source').id.count().reset_index()

print click_source

click_source_by_month = user_visits.groupby(['utm_source', 'month']).id.count().reset_index()

click_source_by_month_pivot = click_source_by_month.pivot(
	columns = 'month',
	index = 'utm_source',
	values = 'id').reset_index()

print click_source_by_month_pivot