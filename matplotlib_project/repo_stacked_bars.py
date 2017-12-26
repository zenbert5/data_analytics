from matplotlib import pyplot as plt
import numpy as np

unit_topics = ['Limits', 'Derivatives', 'Integrals', 'Diff Eq', 'Applications']
As = [6, 3, 4, 3, 5]
Bs = [8, 12, 8, 9, 10]
Cs = [13, 12, 15, 13, 14]
Ds = [2, 3, 3, 2, 1]
Fs = [1, 0, 0, 3, 0]

x = range(5)

# calc bottom of each stacked bar based on sum of lists from offset of existing bar and bar being stacked on

c_bottom = np.add(As, Bs)
#create d_bottom and f_bottom here
d_bottom = np.add(c_bottom, Cs)
f_bottom = np.add(d_bottom, Ds)

# set figure 10x8
# create bar graph stacked and label each
plt.figure(figsize=(10, 8))
plt.bar(range(len(As)), As, label='A')
plt.bar(range(len(Bs)), Bs, bottom=As, label='B')
plt.bar(range(len(Cs)), Cs, bottom=c_bottom, label='C')
plt.bar(range(len(Ds)), Ds, bottom=d_bottom, label='D')
plt.bar(range(len(Fs)), Fs, bottom=f_bottom, label='F')

# create x tick and assign labels
ax = plt.subplot()
ax.set_xticks(range(len(unit_topics)))
ax.set_xticklabels(unit_topics)

# set title and axis labels
plt.title('Grade distribution')
plt.xlabel('Unit')
plt.ylabel('Number of Students')

plt.legend()

plt.show()

plt.savefig('my_stacked_bar.png')