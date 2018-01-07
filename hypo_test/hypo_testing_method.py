import numpy as np
import matplotlib.pyplot as plt

dist_1 = np.genfromtxt("1.csv",  delimiter=",")
dist_2 = np.genfromtxt("2.csv",  delimiter=",")
dist_3 = np.genfromtxt("3.csv",  delimiter=",")
dist_4 = np.genfromtxt("4.csv",  delimiter=",")

#plot your histogram here
plt.hist(dist_1)
plt.show()

plt.hist(dist_2)
plt.show()

plt.hist(dist_3)
plt.show()

plt.hist(dist_4)
plt.show()

not_normal = 4

dist_2_std = np.std(dist_2)
dist_3_std = np.std(dist_3)
ratio = dist_2_std / dist_3_std
print ratio