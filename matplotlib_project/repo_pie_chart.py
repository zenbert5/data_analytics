from matplotlib import pyplot as plt

unit_topics = ['Limits', 'Derivatives', 'Integrals', 'Diff Eq', 'Applications']
num_hardest_reported = [1, 3, 10, 15, 1]

#Make your plot here

# set figure 10x8
plt.figure(figsize=(10, 8))

# draw pie with labels and percentage rounded to int
plt.pie(num_hardest_reported, labels=unit_topics, autopct='%d%%')
# equalize the view
plt.axis('equal')

plt.title('Hardest Topics')

plt.show()

plt.savefig('my_pie_chart.png')