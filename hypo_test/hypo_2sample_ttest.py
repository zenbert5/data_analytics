from scipy.stats import ttest_ind
import numpy as np

week1 = np.genfromtxt("week1.csv",  delimiter=",")
week2 = np.genfromtxt("week2.csv",  delimiter=",")

for i in range(len(week1)):
  print "{},".format(week1[i]),
print '\n'

for i in range(len(week2)):
  print "{},".format(week2[i]),
print '\n'

week1_mean = np.mean(week1)
week2_mean = np.mean(week2)
print week1_mean
print week2_mean

week1_std = np.std(week1)
week2_std = np.std(week2)
print week1_std
print week2_std

pstat, pval = ttest_ind(week1, week2)

print pval