
from matplotlib import pyplot as plt

x = [1970, 1980, 1990, 2000, 2010, 2020]
y1 = [66, 128, 93, 81, 72, 30]
y2 = [12, 73, 55, 32, 40, 10]

plt.plot(x, y1, label='Hits', color='pink', marker='o')
plt.plot(x, y2, label='TopChart Hits', color='gray', marker='o')
plt.xlabel("Amazing X-axis")
plt.ylabel("Incredible Y-axis")
plt.title("Two Lines on One Graph")

plt.legend(loc=4)

plt.show()


"""
clear figure
figure
savefig
"""

word_length = [8, 11, 12, 11, 13, 12, 9, 9, 7, 9]
power_generated = [753.9, 768.8, 780.1, 763.7, 788.5, 782, 787.2, 806.4, 806.2, 798.9]
years = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009]

plt.close('all')

plt.plot(years, word_length)
plt.savefig('winning_word_lengths.png')

plt.figure(figsize=(7,3))
plt.plot(years, power_generated)
plt.savefig('power_generated.png')

"""
label axis
set axis ticks and label

"""
month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep","Oct", "Nov", "Dec"]

months = range(12)
conversion = [0.05, 0.08, 0.18, 0.28, 0.4, 0.66, 0.74, 0.78, 0.8, 0.81, 0.85, 0.85]

plt.xlabel("Months")
plt.ylabel("Conversion")

plt.plot(months, conversion)

# Your work here
ax = plt.subplot()

ax.set_xticks(months)
ax.set_yticks([0.10, 0.25, 0.50, 0.75])
ax.set_xticklabels(month_names)
ax.set_yticklabels(['10%', '25%', '50%', '75%'])


plt.show()


"""
set legend
set legend, labeling, and set legend location
"""
months = range(12)
hyrule = [63, 65, 68, 70, 72, 72, 73, 74, 71, 70, 68, 64]
kakariko = [52, 52, 53, 68, 73, 74, 74, 76, 71, 62, 58, 54]
gerudo = [98, 99, 99, 100, 99, 100, 98, 101, 101, 97, 98, 99]

plt.plot(months, hyrule)
plt.plot(months, kakariko)
plt.plot(months, gerudo)

#create your legend here

legend_labels = ['Hyrule', 'Kakariko', 'Gerudo Valley']

plt.legend(legend_labels, loc=9)

plt.show()

"""
set subplot for formatting multi plot
formatting syntax

"""

x = range(7)
straight_line = [0, 1, 2, 3, 4, 5, 6]
parabola = [0, 1, 4, 9, 16, 25, 36]
cubic = [0, 1, 8, 27, 64, 125, 216]

plt.subplot(2, 1, 1)
plt.plot(x, straight_line)

plt.subplot(2, 2, 3)
plt.plot(x, parabola)

plt.subplot(2, 2, 4)
plt.plot(x, cubic)

plt.subplots_adjust(wspace=0.35, bottom=0.2)

plt.show()