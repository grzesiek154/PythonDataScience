import numpy as np
import matplotlib.pylab as plt

img_original = plt.imread("Sunflower_from_Silesia2.jpg")
img_grayscale = img_original.copy()

for row in range(img_grayscale.shape[0]):
    for col in range(img_grayscale.shape[1]):
        gray = np.average(img_grayscale[row, col])
        img_grayscale[row, col] = (gray, gray, gray)
        
plt.imshow(img_grayscale, interpolation="nearest")
plt.show()