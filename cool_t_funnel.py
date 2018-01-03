"""
	Project	: Cool T-Shirts Inc. data analytics on web
    Company	: Cool T-Shirts Inc.
	Date	: Dec 26, 2017
    Student	: Shawn Chen

--> assumptions:
    a. the reference of 'users' denotes any user related transaction and is NOT specifically a unique user.
    b. for purpose of the assignment (and Cool T-Shirt), factors as related to specific demographics (repeat users incl.) are not being studied; therefore, all user transactions are neutral


"""
import pandas as pd
from matplotlib import pyplot as plt

visits = pd.read_csv('visits.csv',
                     parse_dates=[1])
cart = pd.read_csv('cart.csv',
                   parse_dates=[1])
checkout = pd.read_csv('checkout.csv',
                       parse_dates=[1])
purchase = pd.read_csv('purchase.csv',
                       parse_dates=[1])

# .1 display some rows
print visits.head()
print cart.head()
print checkout.head()
print purchase.head()

# .2 merge on visits preference over cart (time)
visits_cart = pd.merge(visits, cart, how='left')

#. 3 how long is the merged dataframe?
print "Total rows in merge dataframe (visit + cart) is %d" % visits_cart.visit_time.count()

# .4 how many null timestamp on the cart_time?
cart_null = visits_cart[visits_cart.cart_time.isnull()]
print "There were %d of null in cart_time." % cart_null.visit_time.count()

# .5 determine % of visitors didn't place shirt in cart
cart_null_perc = (float(cart_null.user_id.count()) / visits_cart.visit_time.count()) * 100
print " -- equivalent of %.2f%% of visitors didn't place shirt in cart.\n" % cart_null_perc

# .6 determine % of visitors had shirt(s) in cart but didn't checkout
cart_checkout = pd.merge(cart, checkout, how='left')
checkout_null = cart_checkout[cart_checkout.checkout_time.isnull()]
checkout_null_perc = (float(checkout_null.user_id.count()) / cart_checkout.cart_time.count()) * 100
print "%.2f%% of visitors had shirt(s) in cart but didn't checkout.\n" % checkout_null_perc

# .7 merge all dataframes into all_data and print head
all_data = visits.merge(cart, how='left').merge(checkout, how='left').merge(purchase, how='left')

print all_data.head(10)

# .8 determine percentage of user proceeded to checkout but did purchase
no_purchase = all_data[(all_data.checkout_time.notnull() & all_data.purchase_time.isnull())].reset_index()
all_check_plus_purchase = all_data[(all_data.purchase_time.notnull() | all_data.checkout_time.notnull())].reset_index()

no_purchase_users = no_purchase.user_id.count()
all_users = all_check_plus_purchase.user_id.count()
diff_perc = (float(no_purchase_users) / all_users) * 100
print ("Out of the %d total users that completed checkout and or purchase, %.2f%% or %d users did not complete purchase." % (all_users, diff_perc, no_purchase_users))

# .9 illustrate order of magnitude in abandon rate
transaction_type = ['site visit', 'add to cart', 'checkout', 'purchase']
transaction_failure = [0, 80.51, 20.93, 14.71]

plt.figure(figsize=(12, 8))
ax = plt.subplot()
x_values = range(len(transaction_type))
plt.plot(x_values, transaction_failure, marker='*', label='Web Transaction Type Abandon Rate')
plt.ylim(0, 100)
plt.xlabel('Transaction Step')
plt.ylabel('Percentage of Abandonment (%)')
plt.title('Cool T-Shirt Web Traffic Analysis')
ax.set_xticks(x_values)
ax.set_xticklabels(transaction_type)
plt.legend()

plt.subplots_adjust(top=0.90, wspace=0.35)
plt.show()

# .10 - .12 calculate average time from initial visit to purchase
all_data['time_to_purchase'] = all_data.purchase_time - all_data.visit_time
print "Average time for each complete transaction is %s" % all_data.time_to_purchase.mean()
