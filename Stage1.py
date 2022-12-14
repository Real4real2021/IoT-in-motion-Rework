# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 00:26:09 2022

@author: Kris K
"""
#Using contours to specify which objects to focus on

import numpy as np
import cv2

cap = cv2.VideoCapture('')

ret, frame1 = cap.read()
ret, frame2 = cap.read()

while cap.isOpened():
    diff = cv2.absdiff(frame1, frame2)
    grey = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(grey, (5,5), 0)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, 3)
    contours,_ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour)
        
        if cv2.contourArea(contour) < 500:
            continue
        cv2.rectangle(frame1, (x,y), (x+w, y+h), (0,255,0), 2)
        
   # cv2.drawContours(frame1, contours, -1, (0,255,0), 2)

    cv2.imshow('feed', frame1)
    frame1 = frame2
    ret, frame2 = cap.read()
    
    if cv2.waitKey(40) == 27:
        break

cv2.destroyAllWindows()
cap.release()
    

    



