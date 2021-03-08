import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('photos/PP.jpg')
cv.imshow("Me", img)

# BGR to GRAY
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)

# BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow("HSV", hsv)

# BGR to L*a*b
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow("LAB", lab)

# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow("RGB", rgb)

plt.imshow(rgb)
plt.show()

cv.waitKey(0)