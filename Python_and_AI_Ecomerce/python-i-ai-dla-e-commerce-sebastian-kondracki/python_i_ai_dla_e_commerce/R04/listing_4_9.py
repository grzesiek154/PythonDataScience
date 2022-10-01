import numpy as np

a = np.random.rand(5, 5)
b = np.ones((5, 5))
c = np.add(a, b)
d = np.subtract(a, b)
e = np.divide(b, a)
f = np.multiply(a, b)
g = np.exp(a)

print(c)
print(d)
print(e)
print(f)
print(g)