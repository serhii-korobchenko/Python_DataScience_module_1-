# Investor  (50000) -----> Bank1 (5%)  ------ ? initially
#                   -----> Bank2 (7%)  ------ ? initially
#                   -----> Bank3(6 %)  ------ ? initially
#
# Income ----- Bank1 + Bank2 = 2250
#        ----- Bank1 + Bank3 = 1400
#
# 1x + 1y + 1z = 50000
# 0.05x + 0.07y + 0z = 2250
# 0.05x + 0z + 0.06z = 1400


# Result = 10000. - Bank1
#          25000. - Bank2
#          15000. - Bank3

import numpy as np

a = np.matrix("1,1,1;0.05,0.07,0;0.05, 0, 0.06")
b = np.matrix("50000;2250;1400")
a_inv = np.linalg.inv(a)
x = a_inv.dot(b)
print(x)