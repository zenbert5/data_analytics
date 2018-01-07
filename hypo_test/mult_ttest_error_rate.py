from scipy.stats import ttest_ind
import numpy as np

a = np.genfromtxt("store_a.csv",  delimiter=",")
b = np.genfromtxt("store_b.csv",  delimiter=",")
c = np.genfromtxt("store_c.csv",  delimiter=",")

a_mean = np.mean(a)
b_mean = np.mean(b)
c_mean = np.mean(c)
a_std = np.std(a)
b_std = np.std(b)
c_std = np.std(c)

print "Store A mean:{} standard deviation:{}".format(a_mean,a_std)
print "Store B mean:{} standard deviation:{}".format(b_mean,b_std)
print "Store C mean:{} standard deviation:{}".format(c_mean,c_std)

# 2-Sample T-test
pstat, a_b_pval = ttest_ind(a, b)
pstat, a_c_pval = ttest_ind(a, c)
pstat, b_c_pval = ttest_ind(b, c)
print "Store A & B sales difference pval:{}".format(a_b_pval)
print "Store A & C sales difference pval:{}".format(a_c_pval)
print "Store B & C sales difference pval:{}".format(b_c_pval)

error_prob = 1- (0.95**3)

# 3 samples of ttest has increased the prob of error to 14.26%
print error_prob