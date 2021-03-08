import cv2 as cv
import numpy as np

img = cv.imread('photos/PP.jpg')
cv.imshow('Me',img)

blank = np.zeros(img.shape[:2], dtype='uint8')

#Splitting image into color channels
b,g,r = cv.split(img)

blue = cv.merge([b,blank,blank])
green = cv.merge([g,blank,blank])
red = cv.merge([r,blank,blank])

cv.imshow('Blue', blue)
cv.imshow('Green', green)
cv.imshow('Red', red)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

#Merge images to get back the original image
merged = cv.merge([b,g,r])
cv.imshow('Merged', merged)

cv.waitKey(0)