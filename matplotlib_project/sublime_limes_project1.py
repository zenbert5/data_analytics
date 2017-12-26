"""
Project 1 - Sublime Limes
Dec 19, 2017
Shawn Chen

"""

from matplotlib import pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

visits_per_month = [9695, 7909, 10831, 12942, 12495, 16794, 14161, 12762, 12777, 12439, 10309, 8724]

# numbers of limes of different species sold each month
key_limes_per_month = [92.0, 109.0, 124.0, 70.0, 101.0, 79.0, 106.0, 101.0, 103.0, 90.0, 102.0, 106.0]
persian_limes_per_month = [67.0, 51.0, 57.0, 54.0, 83.0, 90.0, 52.0, 63.0, 51.0, 44.0, 64.0, 78.0]
blood_limes_per_month = [75.0, 75.0, 76.0, 71.0, 74.0, 77.0, 69.0, 80.0, 63.0, 69.0, 73.0, 82.0]

# create your figure here
plt.figure(figsize=(12, 8))

ax1 = plt.subplot(1, 2, 1)
x_values = range(len(months))

# .8 - set month distinct value
plt.plot(x_values, visits_per_month, marker='*')

# .9 - axis labels
plt.xlabel('Month of the Year')
plt.ylabel('Visits per Month')

plt.title('Visitors Count over the Year')

# .10-.11 - format x tick
ax1.set_xticks(x_values)
ax1.set_xticklabels(months)



ax2 = plt.subplot(1, 2, 2)
# .12-.13 - 3 lines plot including label and color format
plt.plot(x_values, key_limes_per_month, label='Key Limes', color='#00cc00', marker='o')
plt.plot(x_values, persian_limes_per_month, label='Persian Limes', color='#006600', marker='o')
plt.plot(x_values, blood_limes_per_month, label='Blood Limes', color='#990033', marker='o')

# .14 - add legend using default (best)
plt.legend()

plt.xlabel('Month of the Year')
plt.ylabel('Limes Sold per Month')

plt.title('Limes Sold Per Month by Type')

# .15 - set x-axis to x_values (range of month) and set labels to months
ax2.set_xticks(x_values)
ax2.set_xticklabels(months)


# .16 - adjust the plot to address visual presentation
plt.subplots_adjust(top=0.95, wspace=0.35)

plt.savefig('sublime_lime_annual_report.png')

plt.show()
