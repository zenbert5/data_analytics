"""
    Project: FoodWheel data analytics
    company: FoodWheel, a delivery service startup

    Analyst: Shawn Chen
    Date:    Dec 27, 2017

"""
import pandas as pd
from matplotlib import pyplot as plt
import calendar


# task 1 - pie chart showing restaurants by cuisine type
restaurants = pd.read_csv('restaurants.csv', parse_dates=[1])
restaurants.head()

cuisine_types = restaurants.cuisine.nunique()
print "FoodWheel offers %d types of cuisine." % cuisine_types

cuisine_counts = restaurants.groupby('cuisine').name.count().reset_index()
cuisine_counts.columns = ['cuisine_type', 'restaurant_count']
print cuisine_counts.head()



plt.pie(cuisine_counts['restaurant_count'], autopct='%0.1f%%', labels=cuisine_counts.cuisine_type)
plt.axis('equal')

plt.title('FoodWheel Restaurant Count by Cuisine Type')



# task 2 - bar charts with std of avg sale by month

plt.figure(figsize=(10, 8))
orders = pd.read_csv('orders.csv', parse_dates=[1])

orders['month'] = orders.date.apply(lambda x: x.split('-')[0])
print orders.head()

avg_order = orders.groupby('month').price.mean().reset_index()
std_order = orders.groupby('month').price.std().reset_index()


ax2 = plt.subplot()
plt.bar(range(len(avg_order.month)), avg_order.price, yerr=std_order.price, capsize=5)

avg_order['month_name'] = avg_order.month.apply(lambda x: calendar.month_name[int(x)])

plt.xlabel('Month')
plt.ylabel('Average Sales Price')
plt.title('FoodWheel Average Sales Price by Month')

ax2.set_xticks(range(len(avg_order.month_name)))
ax2.set_xticklabels(avg_order.month_name)

plt.show()

# task 3 - customer types

customer_amount = orders.groupby('customer_id').price.sum().reset_index()
print customer_amount.head()

plt.hist(customer_amount.price, range=(0, 200), bins=40, alpha=0.7)
plt.xlabel('Total Spent')
plt.ylabel('Number of Customers')
plt.title('Customer Spending Spread')

plt.show()