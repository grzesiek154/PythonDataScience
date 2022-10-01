import numpy as np

a = np.load("a_array.npy")
a_b = np.load("a_b_array.npz")
a_b_compressed = np.load("a_b_compressed_array.npz")
print(a)
print(a_b["a"])
print(a_b["b"])
print(a_b_compressed["a"])
print(a_b_compressed["b"])