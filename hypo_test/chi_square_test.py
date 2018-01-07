from scipy.stats import chi2_contingency

# Contingency table
#         harvester |  leaf cutter
# ----+------------------+------------
# 1st gr | 30       |  10
# 2nd gr | 35       |  5
# 3rd gr | 28       |  12
# 4th gr | 20       |  20

X = [[30, 10],
     [35, 5],
     [28, 12],
     [20, 20]]
chi2, pval, dof, expected = chi2_contingency(X)
print pval
