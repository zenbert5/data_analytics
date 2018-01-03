"""
	Project	: Cool T-Shirts Inc. data analytics on web
    Company	: Cool T-Shirts Inc.
	Date		: Dec 26, 2017
    Student	:	Shawn Chen

"""

import pandas as pd

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
unique_users = cart_null.groupby('user_id')['cart_time'].nunique()
print unique_users