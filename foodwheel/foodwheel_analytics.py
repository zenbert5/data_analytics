"""
    Project: FoodWheel data analytics
    company: FoodWheel, a delivery service startup

    Analyst: Shawn Chen
    Date:    Dec 27, 2017

"""
import pandas as pd
from matplotlib import pyplot as plt

restaurants = pd.read_csv('restaurants.csv', parse_dates=[1])

print restaurants.head()

cuisine_types = restaurants.cuisine.nunique()
print "FoodWheel offers %d types of cuisine." % cuisine_types

cuisine_counts = restaurants.groupby('cuisine').name.count().reset_index()
cuisine_counts.columns = ['cuisine_type', 'restaurant_count']
print cuisine_counts

plt.figure(figsize=(10, 8))
plt.subplots()

plt.pie(cuisine_counts['restaurant_count'], autopct='%0.1f%%', labels=cuisine_counts.cuisine_type)
plt.axis('equal')

plt.title('FoodWheel Restaurant Count by Cuisine Type')
plt.subplots_adjust(left=0.085)

plt.show()
