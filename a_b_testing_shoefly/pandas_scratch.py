import pandas as pd


sales = pd.read_csv('sales.csv')
print sales
targets = pd.read_csv('targets.csv')
print targets

sales_vs_targets = pd.merge(sales, targets)

print sales_vs_targets

crushing_it = sales_vs_targets[sales_vs_targets.revenue > sales_vs_targets.target].reset_index(drop=True)

print crushing_it

sales = pd.read_csv('sales.csv')
print sales
targets = pd.read_csv('targets.csv')
print targets
men_women = pd.read_csv('men_women_sales.csv')

all_data = sales.merge(targets).merge(men_women)

print all_data

results = all_data[(all_data.revenue > all_data.target) & (all_data.women > all_data.men)]

print results


orders = pd.read_csv('orders.csv')
print orders
products = pd.read_csv('products.csv')
print products

# merge dataframes based 'product_id', including associating and labeling the matching dataframe to have the same consistent label
orders_products = pd.merge(orders, products.rename(columns={'id': 'product_id'}))
print orders_products

# dataframe merge variant using left_on and right_on option to designate which field to match
orders_products = pd.merge(orders, products,
                          left_on='customer_id',
                          right_on='id',
                          suffixes=['_orders', '_products']
                          )

print orders_products


# outer merge example - use how='outer' in the merge function to dictate outer merge
# by default inner merge is selected and drops non-matching rows
store_a = pd.read_csv('store_a.csv')
print store_a
store_b = pd.read_csv('store_b.csv')
print store_b

store_a_b_outer = pd.merge(store_a, store_b, how='outer')

print store_a_b_outer

# variant of the merge is merge on priority, i.e., left merge on store_a results in all data set in store a but only matching results included in store_b
# reversing the order yields the results in prioritizing store_b over store_a

store_a_b_left = pd.merge(store_a, store_b, how='left')
store_b_a_left = pd.merge(store_b, store_a, how='left')

print store_a_b_left
print store_b_a_left1


# concatenate appends the rows together between the tables or dataframes
bakery = pd.read_csv('bakery.csv')
print bakery
ice_cream = pd.read_csv('ice_cream.csv')
print ice_cream

menu = pd.concat([bakery, ice_cream])

print menu


# example on merging dataframes with user_id as unique key
# time spent on site is extrapolate from delta of visit - checkout
# meantime aggregate is tabulated from the entire data set using .mean() function
visits = pd.read_csv('visits.csv',
                        parse_dates=[1])
checkouts = pd.read_csv('checkouts.csv',
                        parse_dates=[1])

print visits
print checkouts

v_to_c = pd.merge(visits, checkouts)

v_to_c['time'] = v_to_c.checkout_time - v_to_c.visit_time
print v_to_c

print(v_to_c.time.mean())