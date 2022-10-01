import numpy as np

a = np.random.rand(1000000, 5)
print(a)
np.savetxt("a.txt", a)