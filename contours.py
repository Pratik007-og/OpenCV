import cv2 as cv
import numpy as np

img = cv.imread('photos/PP.jpg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("ME", gray)

blank = np.zeros(img.shape, dtype = 'uint8')
cv.imshow('Blank', blank)

blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
cv.imshow('Blue', blur)

canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges', canny)

# ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
# cv.imshow("Thresh", thresh)

contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contours found!')

cv.drawContours(blank, contours, -1, (9,9,255), thickness=1)
cv.imshow("Contours Drawn", blank)

cv.waitKey(0)