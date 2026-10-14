import cv2 as cv
import numpy as np


"""
Captures the video footage from the laptop 

"""
cap = cv.VideoCapture(0) #Getting the laptops video camera footage

if not cap.isOpened():
    print("Error: Could not open the camera")
else:
    print("Camera opened successfuly")

while True:
    #Reading the first camera frame
    ret, frame = cap.read()
    cv.imshow('Frame', frame)
    if cv.waitKey(1) & 0xFF == ord('q'):  #Waits for a key press to close the window
        break

    
cap.release()
cv.destroyAllWindows()   #Closes the window

#Use Haar Cascades to identify a bird, once bird is indentified a screenshot is taken
