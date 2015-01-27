__author__ = 'matic'

import numpy as np
from heuristic_calculations import HeuristicCalculations

raw_documents = [
    "The sky is blue and bright",
    "The sun is bright and it is raining",
    "The sun in the sky is bright",
    "We can see the shining sun, the bright sun",
    "The brightest flashlight is almost brighter than the sun."
]

classes = np.array([0, 0, 0, 1, 1])



calcs=HeuristicCalculations(raw_documents,classes)
print calcs._calculate_all()

from frequency_heuristics import FrequencyBasedHeuristicCalculations

print FrequencyBasedHeuristicCalculations.random.__doc__
print FrequencyBasedHeuristicCalculations.freq_domn_prod.__doc__
#print calcs