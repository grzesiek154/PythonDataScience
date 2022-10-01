import cv2

img_original = cv2.imread("Sunflower_from_Silesia2.jpg")
img_grayscale = cv2.cvtColor(img_original, cv2.COLOR_BGR2GRAY)
cv2.imshow("Image", img_grayscale)
cv2.waitKey(0)
cv2.destroyAllWindows()