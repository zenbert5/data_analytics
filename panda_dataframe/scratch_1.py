import pandas as pd

orders = pd.read_csv('shoefly.csv')

print(orders.head())

orders['shoe_source'] = orders.shoe_material.apply(lambda x: "vegan" if x != 'leather' else "animal")

orders['salutation'] = orders.apply(lambda row: 'Dear Mr. {}'.format(row.last_name) \
    if row.gender == 'male' else 'Dear Ms. {}'.format(row.last_name), axis =1)

print orders