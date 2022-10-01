import numpy as np

a = np.random.rand(1000000, 5)
b = np.zeros((1000000, 5))
print(a)
print(b)
np.save("a_array", a)
np.savez("a_b_array", a=a, b=b)
np.savez_compressed("a_b_compressed_array", a=a, b=b)