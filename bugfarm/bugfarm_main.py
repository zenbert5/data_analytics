"""
BugFarm - Hypothesis Testing for Microtransactions
CodeAcademy
Jan 9, 2018
Shawn Chen
version 1

"""

import pandas as pd
from scipy.stats import chi2_contingency
from scipy.stats import binom_test

# load datafrae
df = pd.read_csv("clicks.csv")
print df.head()

# create new column and fill with conditional data based on click_day
# v1: use pd.notnull() for dataframe null checking
# df['is_purchase'] = df.click_day.apply(lambda x: 'Purchase' if pd.notnull(x) else 'No Purchase')

# v2: use .loc
mask = df.click_day.notnull()
df['is_purchase'] = 'No Purchase'
df.loc[mask, 'is_purchase'] = 'Purchase'

# create new dataframe grouped by group and is_purchase and count each
purchase_counts = df.groupby(['group', 'is_purchase']).user_id.count().reset_index()

print purchase_counts.head()

# load chi-squared table for analysis
groupA_not_purchases = purchase_counts.user_id[0]
groupA_purchases = purchase_counts.user_id[1]
groupB_not_purchases = purchase_counts.user_id[2]
groupB_purchases = purchase_counts.user_id[3]
groupC_not_purchases = purchase_counts.user_id[4]
groupC_purchases = purchase_counts.user_id[5]

contingency = [[groupA_purchases, groupA_not_purchases],
               [groupB_purchases, groupB_not_purchases],
               [groupC_purchases, groupC_not_purchases]]
print contingency

# calculate chi-squared
chi2, pval, dof, expected = chi2_contingency(contingency)

# print pval
print "pval is {}".format(pval)


# -- part 2 ---
# calculate length of df

df_l = len(df)

# calculate % of visitors required to sell at 0.99, 1.99, 4.99 per upgrade kit, respectively
c99_2_1000 = 1000.0 / 0.99
c99_customer_ratio = c99_2_1000 / df_l
print "@ 99c - ratio is {:.4f}".format(c99_customer_ratio)

c199_2_1000 = 1000.0 / 1.99
c199_customer_ratio = c199_2_1000 / df_l
print "@ $1.99 - ratio is {:.4f}".format(c199_customer_ratio)

c499_2_1000 = 1000.0 / 4.99
c499_customer_ratio = c499_2_1000 / df_l
print "@ $4.99 - ratio is {:.4f}".format(c499_customer_ratio)

print purchase_counts

print "pval @ 0.99 purchased - {}".format(binom_test(316, 1666, c99_customer_ratio))
print "pval @ 1.99 purchased - {}".format(binom_test(183, 1666, c199_customer_ratio))
print "pval @ 4.99 purchased - {}".format(binom_test(83, 1666, c499_customer_ratio))