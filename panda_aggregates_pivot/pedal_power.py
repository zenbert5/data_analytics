"""
    Pedal Power Project :: Python with panda
    Dec 23, 2017
    Shawn Chen

"""

import pandas as pd

# fetch data
inventory = pd.read_csv('inventory.csv')

# populate staten island - 10 rows
staten_island = inventory.head(10)

# 1x request for staten island products info
product_request = staten_island.product_description

# 1x request for brooklyn products with seeds
seed_request = inventory[(inventory.location == 'Brooklyn') & (inventory.product_type == 'seeds')]

# new column/field with 'in stock' indicator
inventory['in_stock'] = inventory.apply(lambda row: True if row.quantity > 0 else False, axis=1)

# tabulate total value of each inventory item
inventory['total_value'] = inventory.price * inventory.quantity

# create new product description based on 'type' + 'desc'
combine_lambda = lambda row: \
    '{} - {}'.format(row.product_type,
                     row.product_description)

inventory['full_description'] = inventory.apply(combine_lambda, axis=1)

print inventory