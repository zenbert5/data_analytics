"""
NoshMishMosh - A/B Testing
CodeAcademy
Jan 8, 2018
Shawn Chen
version 1

"""

import noshmishmosh as nmm
import numpy as np

# .4 establish baseline number (of visitors)
all_visitors = nmm.customer_visits

# .5 identify conversion rate
paying_visitors = nmm.purchasing_customers

# .6 identify length of both data sets
total_visitor_count = len(all_visitors)
paying_visitor_count = len(paying_visitors)

# .7 - .8 establish baseline conversion rate
baseline_percent = 100.0 * paying_visitor_count / total_visitor_count
print "baseline conversion rate is {}".format(baseline_percent)

# .9 input payment_history to establish average money spent
payment_history = nmm.money_spent

# .10 determine average payment/customer then delta required to reach $1240
average_payment = np.mean(payment_history)

# .11 determine ceiling value for payment history
new_customers_needed = np.ceil(1240.0 / average_payment)
print "{:d} new customers are needed to reach $1240 in additional revenue.".format(int(new_customers_needed))

# .12 calculate percentage lift
percentage_point_increase = new_customers_needed * 100.0 / total_visitor_count
print "lift required is {}%".format(percentage_point_increase)

# .13 - .14 determine minimum detectable effect
minimum_detectable_effect = percentage_point_increase / baseline_percent * 100.0
print "minimum detectable effect is {:.2f}%".format(minimum_detectable_effect)

# .15 - .16 plug the numbers into calculator to determine sample size
ab_sample_size = 290
print "sample size needs to be {}".format(ab_sample_size)