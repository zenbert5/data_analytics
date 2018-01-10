"""
	Familiar - a study in data analysis
	CodeAcademy 
  Shawn Chen
  Jan 7, 2018

"""

import numpy as np
import familiar as fami
from scipy.stats import ttest_1samp, ttest_ind, chi2_contingency

# .2 load vein pack data
vein_pack_lifespans = fami.lifespans(package='vein')

# .3 calculate vein pack mean 
vein_pack_test = np.mean(vein_pack_lifespans)
print "Average lifespan in Vein Pack Test: {}\n".format(vein_pack_test)

# .4 1sample test on vein pack again avg of 71
pstat, pval = ttest_1samp(vein_pack_lifespans, 71)

# .5 - .6 notify vlad of the result
if pval < 0.05:
    print "The Vein Pack is Proven To Make You Live Longer!\n"
else:
    print "The Vein Pack is Probably Good For You Somehow!\n"

# .7 load artery pack data  
artery_pack_lifespans = fami.lifespans(package='artery')

# .8 2sample test between artery and vein
pstat, package_comparison_results = ttest_ind(artery_pack_lifespans, vein_pack_lifespans)
print "Artery v Vein Pack comparison - pval: {}".format(pval)

# .9 - .11 disclose artery pack findings
if package_comparison_results < 0.05:
    print "The Artery Package Guarantees Even Stronger Results!\n"
else:
    print "The Artery Package is Also A Great Product!\n"

# .12 - .13 contingency spin on the artery pack, load iron count for packages
iron_contingency_table = fami.iron_counts_for_package()

# .14 - .16 run chi-square test on iron_contingency
chi2, iron_pval, dof, expected = chi2_contingency(iron_contingency_table)
print "Chi-Squared Test - pval: {}".format(iron_pval)

if iron_pval < 0.05:
    print "The Artery Package Is Proven To Make You Healthier!"
else:
    print "While We Can't Say The Artery Package Will Help You, I Bet It's Nice!"