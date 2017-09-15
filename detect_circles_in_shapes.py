import cv2
import numpy as np


img = cv2.imread('imagens/shapes_leo.jpg')
cv2.imshow('original',img)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

kernel = np.ones((9,9),np.uint8)

img = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

#cv2.imshow('opening',img)

img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

#cv2.imshow('closing',img)

cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)

circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 20,
                           param1=50, param2=40, minRadius=10, maxRadius=0)
if circles != None:
    circles = np.uint16(np.around(circles))
    for i in circles[0,:]:
        # draw the outer circle
        cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
        # draw the center of the circle
        cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)
    cv2.imshow('detected circles',cimg)

cv2.waitKey(0)
cv2.destroyAllWindows()