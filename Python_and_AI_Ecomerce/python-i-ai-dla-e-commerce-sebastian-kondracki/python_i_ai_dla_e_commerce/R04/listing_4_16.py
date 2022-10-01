import numpy as np
import matplotlib.pylab as plt

img_original = plt.imread("Sunflower_from_Silesia2.jpg")
img = img_original.copy()
img_grayscale = img.copy()

r, g, b = (
    (np.array(img[:, :, 0]) * 0.2989),
    (np.array(img[:, :, 1])) * 0.5870,
    (np.array(img[:, :, 2])) * 0.1140,
)

gray = r + g + b
for i in range(3):
    img_grayscale[:, :, i] = gray
plt.imshow(img_grayscale, interpolation="nearest")
plt.show()
