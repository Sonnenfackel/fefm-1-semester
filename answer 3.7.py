import numpy as np
a = ([[1.,3.,3.],
      [4.,5.,6.],
      [7.,8.,9.]])
D = np.linalg.det(a)
b = ([1.,2.,3.])
x = []
for i in range(len(b)):
    m1 = np.copy(a)
    m1[:,i] = b
    d = np.linalg.det(m1)/D
    x.append(d)
print(x)