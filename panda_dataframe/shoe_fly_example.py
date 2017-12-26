import pandas as pd

orders = pd.read_csv('shoefly.csv')

print(orders)

emails = orders.email

frances_palmer = orders[(orders.first_name == 'Frances') & (orders.last_name == 'Palmer')]

comfy_shoes = orders[orders.shoe_type.isin(['clogs', 'boots', 'ballet flats'])]

new_comfy_shoes = comfy_shoes.reset_index(drop=True)

print(new_comfy_shoes)