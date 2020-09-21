#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 05:36:27 2020

@author: kemistree4
"""

import numpy as np
import cv2 as cv
import argparse

cap = cv.VideoCapture(-1)

while True:
    ret, frame = cap.read()
    color = cv.cvtColor(frame, cv.COLOR_BGR2BGRA) 
    #Color space conversion. There are 150 of these?!?! Why so many?
    
    cv.imshow('frame',color)
    if cv.waitKey(1) & 0xFF == ord('q'): 
        #looks every second to see if the q key is being pressed. If it is then it breaks out of the loop
        break
    
cap.release() #Releases the webcam
cv.destroyAllWindows() #closes all imshow() windows

