import pandas as pd

"""
1. Clean out of the machine, temperate
2. Dirty worn for hot long trip 
3. Sport clothes temperature: cold
4. Sport clothes temperature: hot
5. Long normal days 
6. Worn 2 days long left out 3
7. Work dinner 
8. Not worn but left out
9. Worn one normal day
10. Work short days 
"""
                                        #    1  2   3    4     5  6  7     8  9  10
CLOTHES = pd.DataFrame({'Days_worn':        [0, 5,  1,   1,    2, 2, 1,    0, 1, 3],
                        'Days_left_out':    [0, 5,  0,   0,    0, 3, 0,    3, 0, 0],
                        'Activity':         [0, 5,  5,   5,    1, 1, 0,    0, 1, 1],
                        'Stress':           [0, 5,  1.5, 1.5,  2, 2, 2.5,  0, 2, 2],
                        'Temperature':      [3, 5,  1,   5,    3, 3, 4,    2, 3, 3], 
                        'Hours':            [0, 5,  1,   1,    4, 3, 1.5,  0, 3, 1],
                        'Output': ['clean', 'dirty', 'dirty', 'dirty', 'somewhat dirty', 'somewhat dirty', 'somewhat clean', 'clean', 'somewhat clean', 'somewhat clean']})

# 5, 6, 7, 8, 9, 10