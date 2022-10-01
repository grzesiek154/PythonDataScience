import numpy as np
import matplotlib.pylab as plt

img = plt.imread("Sunflower_from_Silesia2.jpg")
print(img.shape)
plt.imshow(img, interpolation="nearest")
plt.show()