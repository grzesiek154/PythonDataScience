import numpy as np
import matplotlib.pylab as plt

img_original = plt.imread("Sunflower_from_Silesia2.jpg")
img_grayscale = img_original.copy()
for row in range(img_grayscale.shape[0]):
    for col in range(img_grayscale.shape[1]):
        r = img_grayscale[row, col, 0]
        g = img_grayscale[row, col, 1]
        b = img_grayscale[row, col, 2]
        gray = 0.2989 * r + 0.5870 * g + 0.1140 * b
        img_grayscale[row, col] = (gray, gray, gray)
plt.imshow(img_grayscale, interpolation="nearest")
plt.show()