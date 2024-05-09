from simpful import *

FS = FuzzySystem()

"""
Questions we ask:
1. How many days worn
2. How many days left out
3. Level of activity in clothes
4. Level of stress in clothes
5. Weather (hot/col/humid)?
6. How long did you wear it?
"""

# Days worn variable
DW_1 = FuzzySet(function=Trapezoidal_MF(0, 0, 1, 1.5), term='one')
DW_2 = FuzzySet(function=Trapezoidal_MF(1, 1.5, 2, 2.5), term='two')
DW_3 = FuzzySet(function=Trapezoidal_MF(2, 2.5, 3, 3.5), term='three')
DW_4 = FuzzySet(function=Trapezoidal_MF(3, 3.5, 4, 4.5), term='four')
DW_5 = FuzzySet(function=Trapezoidal_MF(4, 4.5, 5, 5), term='five')
LV1 = LinguisticVariable([DW_1, DW_2, DW_3, DW_4, DW_5], concept='Days worn', universe_of_discourse=[0, 5])
FS.add_linguistic_variable('Days_worn', LV1)
LV1.plot()

# Days left out variable
DO_1 = FuzzySet(function=Trapezoidal_MF(0, 0, 1, 1.5), term='one')
DO_2 = FuzzySet(function=Trapezoidal_MF(1, 1.5, 2, 2.5), term='two')
DO_3 = FuzzySet(function=Trapezoidal_MF(2, 2.5, 3, 3.5), term='three')
DO_4 = FuzzySet(function=Trapezoidal_MF(3, 3.5, 4, 4.5), term='four')
DO_5 = FuzzySet(function=Trapezoidal_MF(4, 4.5, 5, 5), term='five')
LV2 = LinguisticVariable([DO_1, DO_2, DO_3, DO_4, DO_5], concept='Days left out', universe_of_discourse=[0, 5])
FS.add_linguistic_variable('Days_left_out', LV2)
LV2.plot()

# Activity intensity variable
A_1 = FuzzySet(function=Trapezoidal_MF(0, 0, 1, 1.5), term='none')
A_2 = FuzzySet(function=Trapezoidal_MF(1, 1.5, 2, 2.5), term='some')
A_3 = FuzzySet(function=Trapezoidal_MF(2, 2.5, 3, 3.5), term='medium')
A_4 = FuzzySet(function=Trapezoidal_MF(3, 3.5, 4, 4.5), term='a_lot')
A_5 = FuzzySet(function=Trapezoidal_MF(4, 4.5, 5, 5), term='full')
LV3 = LinguisticVariable([A_1, A_2, A_3, A_4, A_5], concept='Activity done', universe_of_discourse=[0, 5])
FS.add_linguistic_variable('Activity', LV3)
LV3.plot()

# Stress level variable
S_1 = FuzzySet(function=Trapezoidal_MF(0, 0, 1, 1.5), term='none')
S_2 = FuzzySet(function=Trapezoidal_MF(1, 1.5, 2, 2.5), term='some')
S_3 = FuzzySet(function=Trapezoidal_MF(2, 2.5, 3, 3.5), term='medium')
S_4 = FuzzySet(function=Trapezoidal_MF(3, 3.5, 4, 4.5), term='a_lot')
S_5 = FuzzySet(function=Trapezoidal_MF(4, 4.5, 5, 5), term='full')
LV4 = LinguisticVariable([S_1, S_2, S_3, S_4, S_5], concept='Stress level', universe_of_discourse=[0, 5])
FS.add_linguistic_variable('Stress', LV4)
LV4.plot()

# Temperature variable
T_1 = FuzzySet(function=Trapezoidal_MF(0, 0, 1, 1.5), term='hot')
T_2 = FuzzySet(function=Trapezoidal_MF(1, 1.5, 2, 2.5), term='warm')
T_3 = FuzzySet(function=Trapezoidal_MF(2, 2.5, 3, 3.5), term='temperate')
T_4 = FuzzySet(function=Trapezoidal_MF(3, 3.5, 4, 4.5), term='fresh')
T_5 = FuzzySet(function=Trapezoidal_MF(4, 4.5, 5, 5), term='cold')
LV5 = LinguisticVariable([T_1, T_2, T_3, T_4, T_5], concept='Outside temperature', universe_of_discourse=[0, 5])
FS.add_linguistic_variable('Temperature', LV5)
LV5.plot()

# Hours worn variable
H_1 = FuzzySet(function=Trapezoidal_MF(0, 0, 1, 1.5), term='two')
H_2 = FuzzySet(function=Trapezoidal_MF(1, 1.5, 2, 2.5), term='four')
H_3 = FuzzySet(function=Trapezoidal_MF(2, 2.5, 3, 3.5), term='six')
H_4 = FuzzySet(function=Trapezoidal_MF(3, 3.5, 4, 4.5), term='twelve')
H_5 = FuzzySet(function=Trapezoidal_MF(4, 4.5, 5, 5), term='more')
LV6 = LinguisticVariable([H_1, H_2, H_3, H_4, H_5], concept='Hours per day', universe_of_discourse=[0, 5])
FS.add_linguistic_variable('Hours', LV6)
LV6.plot()

# Output variable
O_1 = FuzzySet(function=Triangular_MF(0, 0, 0.5), term='dirty')
O_2 = FuzzySet(function=Triangular_MF(0.5, 1, 1), term='clean')
LV7 = LinguisticVariable([O_1, O_2], concept='Cleanliness', universe_of_discourse=[0, 1])
FS.add_linguistic_variable('Output', LV7)


# Rules
R1 = "IF " \
     "(Days_worn IS five) OR " \
     "(Days_left_out IS five) OR " \
     "(Activity IS full) OR " \
     "(Stress IS full) OR " \
     "(Temperature IS hot) " \
     "(Hours IS more) OR " \
     "THEN " \
     "(Output IS dirty)"
R2 = "IF " \
     "(Days_worn IS one) OR " \
     "(Days_left_out IS one) OR " \
     "(Activity IS full) OR " \
     "(Stress IS full) OR " \
     "(Temperature IS hot) " \
     "(Hours IS more) OR " \
     "THEN " \
     "(Output IS dirty)"
R3 = "IF " \
     "(Days_worn IS five) OR " \
     "(Days_left_out IS five) OR " \
     "(Activity IS full) OR " \
     "(Stress IS full) OR " \
     "(Temperature IS hot) " \
     "(Hours IS more) OR " \
     "THEN " \
     "(Output IS dirty)"



