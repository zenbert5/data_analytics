"""
    CrunchieMunchies Project

    Python with matplotlib, pandas & numpy

    Shawn Chen
    Jan 2, 2018

"""

from matplotlib import pyplot as plt
import numpy as np

# .2 - load data into numpy array
calorie_stats = np.genfromtxt('cereal.csv', delimiter=',')

sample_set_size = len(calorie_stats)

# .3 - find the average calorie of competitors
average_calorie = np.mean(calorie_stats)
print "Average calorie in sample is %d" % average_calorie

# .4 - what's the average distribution? sort
sorted_calorie = np.sort(calorie_stats)
print sorted_calorie


# .5 - calc median to reference against the skew
median_calorie = np.median(calorie_stats)
print "median calorie is %d" % median_calorie


# .6 - calculate percentiles
"""
for x in range(1,101):
    if (np.percentile(sorted_calorie, x) > 100):
        low_perc = x
        break
        
"""
low_perc = np.mean(sorted_calorie <=100)
print "Lowest percentile with more than 100 calories is %.2f%%" % low_perc

one_std = np.percentile(sorted_calorie, 68)
two_std = np.percentile(sorted_calorie, 95)
three_std = np.percentile(sorted_calorie, 99.7)

# .7 - percentage of cereals with 100 or more cal
high_calorie = np.mean(calorie_stats >= 100) * 100.0
print "%.2f%% of all cereal brands sampled are more than 100 calories" % high_calorie
cm_perc = (1.00 - np.mean(calorie_stats <= 70)) * 100.0


# .8 - determine standard deviation
calorie_std = np.std(sorted_calorie)
print "Standard deviation is %.2f%%" % calorie_std
print " Ref 1-2-3 deviations: %.2f, %.2f, %2.f 68/95/99.7\n" % (one_std, two_std, three_std)

print "Based on the competitive study performed on %d cereals, CrunchieMunchies is over 30%% lower in calorie comparing with the average of 106 calories and a median of 110 calories.  Over %.2f%% of cereal brands are higher in calorie than C.M." % (sample_set_size, cm_perc)
print "CrunchieMunchies is in an excellent position to market as a healthy option to the alternatives."