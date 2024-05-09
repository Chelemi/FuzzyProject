import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
from skfuzzy import membership as mf
import pandas as pd

# Output
cloth_state = ['dirty', 'clean']

"""
Questions we ask:
1. How many days worn
2. How many days left out
3. Level of activity in clothes
4. Level of stress in clothes
5. Weather (hot/col/humid)?
6. How long did you wear it?
"""

# Input
informations = ['days_worn',
                'days_left_out',
                'activity',
                'stress',
                'weather',
                'hours_worn']

# Define the possible responses
days_worn = np.arange(0, 6, 1)  # 1, 2, 3, 4, >5
days_left_out = np.arange(0, 6, 1)  # 1, 2, 3, 4, >5
activity = np.arange(0, 6, 1)  # none, some, medium, a lot, only activity
stress = np.arange(0, 6, 1)  # none, some , medium, a lot, the whole time
temperature = np.arange(0, 6, 1)  # hot, warm, temperate, fresh, cold
hours_worn = np.arange(0, 6, 1)  # <2, 2-4, 4-6, 6-12, >12
outputs = np.arange(0, 2, 1)  # dirty, clean

# Create the different features (fuzzy logic variables)
feature1 = ctrl.Antecedent(days_worn, 'days_worn')
feature2 = ctrl.Antecedent(days_left_out, 'days_left_out')
feature3 = ctrl.Antecedent(activity, 'activity')
feature4 = ctrl.Antecedent(stress, 'stress')
feature5 = ctrl.Antecedent(temperature, 'temperature')
feature6 = ctrl.Antecedent(hours_worn, 'hours_worn')
output = ctrl.Consequent(outputs, 'output')

# Define the membership functions
feature1.automf(names=['1', '2', '3', '4', '>5'])
feature2.automf(5)
feature3.automf(5)
feature4.automf(5)
feature5.automf(5)
feature6.automf(5)
output.automf(names=['dirty', 'clean'])





