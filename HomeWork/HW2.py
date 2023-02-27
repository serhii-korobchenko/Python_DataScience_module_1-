# ---IPhone 6   --        x
# ---IPhone 11  --        y
# ---IPhone 12  --        z
# __________________________________all: 1328
#
# x + y + z = 1328               1x + 1y + 1z = 1328
# x = y - 120          ===>      1x + (-1)y + 0z = -120
# x = z + 100                    1x + 0y + (-1)z = 100

#Result:
#---IPhone 6   --         436
# ---IPhone 11  --        556
# ---IPhone 12  --        336



import numpy as np

a = np.matrix("1,1,1;1,-1,0;1, 0, -1")
b = np.matrix("1328;-120;100")
a_inv = np.linalg.inv(a)
x = a_inv.dot(b)
print(x) # result
print (x.sum()) # check