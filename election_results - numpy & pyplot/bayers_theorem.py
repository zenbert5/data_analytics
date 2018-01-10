
"""

    In this course, we learned several new definitions:

    Two events are independent if the occurrence of one event does not affect the probability of the second event
    If two events are independent then,
    P(A ∩ B) = P(A) × P(B)

    A prior is an additional piece of information that tells us how likely an event is
    A frequentist approach to statistics does not incorporate a prior
    A Bayesian approach to statistics incorporates prior knowledge

"""



import numpy as np

a = 'spam'
b = 'enhancement'

p_spam = 0.20
p_non_spam = 0.80
p_enhancement_non_spam = 0.001
p_enhancement_given_spam = 0.05

p_enhancement = p_enhancement_given_spam * p_spam + p_enhancement_non_spam * p_non_spam

# prob of p(s|e) = p (e|s) * p(s) / p(e)
p_spam_enhancement = p_enhancement_given_spam * p_spam / p_enhancement

print p_spam_enhancement