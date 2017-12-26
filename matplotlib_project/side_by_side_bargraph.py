from matplotlib import pyplot as plt

"""
drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
sales =  [91, 76, 56, 66, 52, 27]

plt.bar(range(len(sales)), sales)

#create your ax object here
ax = plt.subplot()
ax.set_xticks(range(len(drinks)))
ax.set_xticklabels(drinks)
"""

drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
sales1 =  [91, 76, 56, 66, 52, 27]
sales2 = [65, 82, 36, 68, 38, 40]


# sales set 1
n = 1  # This is our first dataset (out of 2)
t = 2 # Number of datasets
d = 6 # Number of sets of bars (len(sales1))
w = 0.8 # Width of each bar
store1_x = [t*element + w*n for element in range(d)]

# sales set 2
n = 2  # This is our first dataset (out of 2)
t = 2 # Number of datasets
d = 6 # Number of sets of bars (len(sales1))
w = 0.8 # Width of each bar
store2_x = [t*element + w*n for element in range(d)]
plt.bar(store2_x, sales2)

plt.bar(store1_x, sales1)

plt.show()