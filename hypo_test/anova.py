from scipy.stats import ttest_ind
from scipy.stats import f_oneway
import numpy as np

a = np.genfromtxt("store_a.csv",  delimiter=",")
b = np.genfromtxt("store_b.csv",  delimiter=",")
c = np.genfromtxt("store_c.csv",  delimiter=",")

tstat, pval = f_oneway(a, b, c)
print pval

b = np.genfromtxt("store_b_new.csv", delimiter=",")
tstat, pval = f_oneway(a, b, c)
print pval