import cv2 as cv

img = cv.imread('photos/PP.jpg')
cv.imshow('Me',img)

def changeRes(width, height):
    #Only works for live video
    capture.set(3, width)
    capture.set(4, height)

def rescaleFrame(frame, scale = 0.75):
    #Works for images, videos, live videos
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)

resized_image = rescaleFrame(img)
cv.imshow('Resized_image', resized_image)

capture = cv.VideoCapture('videos/video.mp4')
while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame)
    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xff == ord('d'):
        break



capture.release()
cv.destroyAllWindows()
cv.waitKey(0)