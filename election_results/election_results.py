"""
    Candidate survey exercise - model election result using binomial modeling

    objectives: use of numpy random.binomial function for modeling and np.mean to calculate percent probability


"""

import numpy as np
from matplotlib import pyplot as plt

survey_responses = ['Ceballos', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos','Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos',
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos',
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos',
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos']

actual_ceballos = 0.54
large_size = 7000.0

# .2 tabulate matching
total_ceballos = survey_responses.count('Ceballos')
print '{} voted for Ceballos'.format(total_ceballos)

# .3 calculate percentage of survey that voted Ceballos
percentage_ceballos = 100.0 * total_ceballos / len(survey_responses)
print '{:5.2f}% of people voted for Ceballos'.format(percentage_ceballos)

# .4 - .5 tabulate binomal prob and plot graph
possible_surveys = np.random.binomial(len(survey_responses), actual_ceballos, size=10000) / float(len(survey_responses))
plt.hist(possible_surveys, bins=20, range=(0,1))
plt.xlabel('Percentage')
plt.ylabel('# of experiements(vote)')
plt.title('Model Kerrigan v. Ceballos Election')
plt.show()

# .6 percentile where Ceballos < 50%
ceballos_loss_surveys = np.mean(possible_surveys < .50) * 100.0
print '{:5.2f}% of possibility Ceballos lost (<50%)'.format(ceballos_loss_surveys)

# .7 larger survey
large_survey = np.random.binomial(large_size, 0.54, size=10000) / float(large_size)
ceballos_loss_new = np.mean(large_survey < 0.50) * 100.0
print '{0:5.2f}% of possibility Ceballos lost (<50%) with size of {1}'.format(ceballos_loss_new,large_size)

"""
	Note: larger survey size provides better gauge of actual vs. theoretical
"""