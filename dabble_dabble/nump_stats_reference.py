import numpy as np
# Write matplotlib import here:
from matplotlib import pyplot as plt

commutes = np.genfromtxt('commutes.csv', delimiter=',')

# Plot histogram here:
plt.hist(commutes, bins=8, range=(20, 50))

plt.show()

import codecademylib
import numpy as np
from matplotlib import pyplot as plt

emails = np.random.binomial(500, 0.05, size=10000)

plt.hist(emails)

plt.show()

## Random Norm/Binomials

import numpy as np
from matplotlib import pyplot as plt

sunflowers = np.genfromtxt('sunflower_heights.csv',
                           delimiter=',')

# Calculate mean and std of sunflowers here:
sunflowers_mean = np.mean(sunflowers)
sunflowers_std = np.std(sunflowers)

# Calculate sunflowers_normal here:
sunflowers_normal = np.random.normal(sunflowers_mean, sunflowers_std, size=5000)

plt.hist(sunflowers,
         range=(11, 15), histtype='step', linewidth=2,
        label='observed', normed=True)
plt.hist(sunflowers_normal,
         range=(11, 15), histtype='step', linewidth=2,
        label='normal', normed=True)
plt.legend()
plt.show()