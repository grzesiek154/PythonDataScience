import numpy as np
import matplotlib.pylab as plt

img = np.zeros((3, 3, 3))
img[0, 1] = (255, 255, 255)
img[1, 0] = (255, 255, 255)
img[1, 2] = (255, 255, 255)
img[2, 1] = (255, 255, 255)
plt.imshow(img)
plt.show()