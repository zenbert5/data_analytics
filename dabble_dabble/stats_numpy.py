import numpy as np
# Write matplotlib import here:
from matplotlib import pyplot as plt


emails = np.random.binomial(500, 0.05, size=10000)

no_emails = np.mean(emails == 0)

print no_emails