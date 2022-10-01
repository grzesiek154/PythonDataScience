import numpy as np
import matplotlib.pylab as plt

img_original = plt.imread("Sunflower_from_Silesia2.jpg")
print("Rozmiar oryginału", img_original.shape)
img_90 = np.rot90(img_original)
print("Rozmiar obróconego obrazu", img_90.shape)
plt.imshow(img_90, interpolation="nearest")
plt.show()
img_croped = img_original[400:1297, 400:2034]
print("Rozmiar wyciętego obrazu", img_croped.shape)
plt.imshow(img_croped, interpolation="nearest")
plt.show()