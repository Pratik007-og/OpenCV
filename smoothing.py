import cv2 as cv

img = cv.imread('photos/PP.jpg')
cv.imshow('Me',img)

#Averging
average = cv.blur(img, (3,3))
cv.imshow('Average blue', average)

#Gaussian 
gaussian = cv.GaussianBlur(img, (3,3), 0)
cv.imshow('Gaussian', gaussian)

# Median Blur
median = cv.medianBlur(img, 3)
cv.imshow('Median', median)

# Bilateral 
bilateral = cv.bilateralFilter(img, 10, 20, 20)
cv.imshow('Bilateral', bilateral)

cv.waitKey(0)