import numpy as np

small_set = [10100, 35500, 105000, 85000, 25500, 40500, 65000]

sorted_small_set = np.sort(small_set)

def find_median(x):
    y = int(len(x) / 2)
    if ((len(x)) % 2) == 1:
        return x[y]
    else:
        return sum(x[y-1:y])

small_set_median = find_median(sorted_small_set)

print small_set_median

##


time_spent = np.genfromtxt('file.csv', delimiter=',')

print time_spent

minutes_mean = np.mean(time_spent)
minutes_median = np.median(time_spent)

print minutes_mean
print minutes_median

best_measure = minutes_median


##

pumpkin = np.array([68, 1820, 1420, 2062, 704, 1156, 1857, 1755, 2092, 1384])

acorn_squash = np.array([20, 43, 99, 200, 12, 250, 58, 120, 230, 215])

pumpkin_avg = np.mean(pumpkin)
acorn_squash_avg = np.mean(acorn_squash)

pumpkin_std = np.std(pumpkin)
acorn_squash_std = np.std(acorn_squash)

def max_std(x,y):
  if x > y:
    return pumpkin
  elif y > x:
    return acorn_squash

winner = max_std(pumpkin_std, acorn_squash_std)

##

rainfall = np.array([5.21, 3.76, 3.27, 2.35, 1.89, 1.55, 0.65, 1.06, 1.72, 3.35, 4.82, 5.11])

rain_mean = np.mean(rainfall)

rain_median = np.median(rainfall)

first_quarter = np.percentile(rainfall, 25)
third_quarter = np.percentile(rainfall, 75)

interquartile_range = third_quarter - first_quarter

rain_std = np.std(rainfall)

print "Average ranfall is %.2f" % rain_mean
print "First & Third Quartiles are %.2f and %.2f" % (first_quarter,third_quarter)
print "Interquartile range is %.2f" % interquartile_range
print "Standard deviation is %.2f" % rain_std

print rain_mean
print first_quarter
print third_quarter
print interquartile_range
print rain_std