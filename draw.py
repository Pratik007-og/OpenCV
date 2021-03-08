import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype = 'uint8')
cv.imshow('Blank image',blank)

# blank[200'p3:300, 300:400] = 0,0,255
# cv.imshow('Red',blank)

# ##Draw Rectangle
# cv.rectangle(blank, (0,0), (200,200), (0,255,0), thickness = -1)
# cv.imshow('Rectangle', blank)

# ##Draw Circle
# cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2),40, (0,0,255), thickness = 2)
# cv.imshow('Circle', blank)

# ##Draw line
# cv.line(blank, (0,0),(blank.shape[1]//2, blank.shape[0]//2),(255,0,0), thickness = 3)
# cv.imshow('Line', blank)

##Text on image
cv.putText(blank, 'Hello', (225,255), cv.FONT_HERSHEY_TRIPLEX, 4.0, (0,255,255), thickness=4)
cv.imshow('Text', blank)

# img = cv.imread('photos/PP.jpg')
# cv.imshow('Me', img)

cv.waitKey(0)