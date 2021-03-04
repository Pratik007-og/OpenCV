import cv2 as cv

img = cv.imread('photos/PP.jpg')
cv.imshow('Me',img)

# ## Converting to GREY SCALE
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray scale', gray)

## Blue
blur = cv.GaussianBlur(img, (5,5), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

## Edge cascade
canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges', canny)

## Dialating the image
dilated = cv.dilate(canny, (3,3), iterations = 3)
cv.imshow('Dialated', dilated)

## Eroding the image
eroded = cv.erode(dilated, (3,3), iterations = 5)
cv.imshow('Eroded', eroded)

## Resize
resized = cv.resize(img, (500,500))
cv.imshow('Resized', resized)

## Cropping
cropped = img[50:400, 100:400]
cv.imshow('Cropped', cropped) 

cv.waitKey(0)