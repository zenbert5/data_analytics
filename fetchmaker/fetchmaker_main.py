"""
	FetchMaker Project
    CodeAcademy: Data Analytics

    Shawn Chen
    Jan 7, 2018

"""

import numpy as np
import fetchmaker as fm
from scipy.stats import binom_test, f_oneway, ttest_ind, chi2_contingency
from statsmodels.stats.multicomp import pairwise_tukeyhsd

# .3 tail average of rottweiler
rottweiler_tl = fm.get_tail_length("rottweiler")

print "Average tail length of rottweiler is {} with standar deviation of {}\n".format(np.mean(rottweiler_tl), np.std(rottweiler_tl))

# .4 - .8 check significance of whippet rescue figure v 8% expectation
whippet_rescue = fm.get_is_rescue("whippet")

num_whippet_rescues = np.count_nonzero(whippet_rescue)
num_whippets = np.size(whippet_rescue)

pval = binom_test(num_whippet_rescues, num_whippets, p=0.08)
print "Actual Whippet rescue v 8% target yield pval of {}\n".format(pval)

# .9 check weight average between 3 breeds
whippet_weight = fm.get_weight("whippet")
terrier_weight = fm.get_weight("terrier")
pitbull_weight = fm.get_weight("pitbull")

whippet_weight_avg = np.mean(whippet_weight)
terrier_weight_avg = np.mean(terrier_weight)
pitbull_weight_avg = np.mean(pitbull_weight)
print "Average weight of whippet is {}, terrier is {}, and pitbull is {}\n".format(whippet_weight_avg, terrier_weight_avg, pitbull_weight_avg)

tstat, weight_avg_pval = f_oneway(whippet_weight, terrier_weight, pitbull_weight)
if weight_avg_pval < 0.05:
  print "There isn't a significant difference between the breeds based on weight.\n"
else:
  print "Weight differs between the breeds.\n"

# .10 determine if any two breeds differ in weight
pstat, w_t_pval = ttest_ind(whippet_weight, terrier_weight)
pstat, w_p_pval = ttest_ind(whippet_weight, pitbull_weight)
pstat, t_p_pval = ttest_ind(terrier_weight, pitbull_weight)

print "Whippet v Terrier weight - pval {}".format(w_t_pval)
print "Whippet v Pitbull weight - pval {}".format(w_p_pval)
print "Terrier v Pitbull weight - pval {}".format(t_p_pval)

# .11 compare poodle and shihtzu colors breakdown
poodle_colors = fm.get_color("poodle")
shihtzu_colors = fm.get_color("shihtzu")

# .12 - .13 create chi_square test of poodle vs shihtzu based on colors
unique_col = np.unique(poodle_colors)
color_table = [[0 for x in (0,1)] for y in range(len(unique_col))]
for i in range(len(unique_col)):
  color_table[i][0] = np.count_nonzero(poodle_colors == unique_col[i])
  color_table[i][1] = np.count_nonzero(shihtzu_colors == unique_col[i])

chi2, pval, dof, expected = chi2_contingency(color_table)

print "Poodle v Shihtzu yield pval of {:.4f}".format(pval)

# .14 extra fun
p_age = fm.get_age("poodle")
r_age = fm.get_age("rottweiler")
w_age = fm.get_age("whippet")

vrt = np.concatenate([p_age, r_age, w_age])
labels = ["Poodle"] * len(p_age) + ["Rottweiler"] * len(r_age) + ["Whippet"] * len(w_age)

t_result = pairwise_tukeyhsd (vrt, labels, 0.05)
print t_result