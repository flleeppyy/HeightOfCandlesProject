# import librarys
import numpy as np # i dont think i even use this at all
import cv2 # This is the library we will use to do things with the webcam and manipulate the image we get from it
#learning this library was a pain and I haven't been fully exposed to its capabilitys
import time # t i m e 

cap = cv2.VideoCapture(1) # set our video capture device, or the webcam

def onMouse(event, x, y, flags, param): # this entire function is to identify coordinates when you clicked inside the window
    if event == cv2.EVENT_LBUTTONDOWN: # if we detect that the left mouse was clicked
       print('x = %d, y = %d'%(x, y)) # print those coords where the mouse was clicked
cv2.setMouseCallback('cropped image with line', onMouse) # make sure the callback is set to the final window

while True: # run everything inside this codeblock endlessly until we encounter a break or interupt
    ret, frame = cap.read() #set the variables (not really variables but constants) to cap.read() meaning were reading the frames directly from the webcam

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # convert the image to grayscale
    ret,thresh1 = cv2.threshold(gray,140,255,cv2.THRESH_BINARY) #create a brightness threshhold so we can try to get only the candle and not the background
    cropped = thresh1[100:265, 180:350] #y, x format : pt1:x272:y100,  pt2:x350:y200 # crop the image so its a smaller picture to mess with
    


    
    #cv2.imshow('original', frame) #create a window with the frames being processed
    cv2.imshow('#1 grayscale image', gray) #create a window with the frames being processed
    cv2.imshow('#2 grayscale with threshold', thresh1) 
    cv2.imshow('#3 cropped image', cropped) 

    
    croplines = cv2.cvtColor(cropped, cv2.COLOR_GRAY2BGR)
    croplines1 = cv2.line(croplines, (110, 0), (110, 272), (0, 0, 255)) # B, G, R because REASONS # also in x, y format
    croppedwithlines = cv2.line(croplines1, (0, 155), (250, 155), (0, 255, 0)) # B, G, R because REASONS # also in x, y format
    cv2.imshow('cropped image with line', croppedwithlines) 
    cv2.setMouseCallback('cropped image with line', onMouse)
    #print("Pass")
    
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

    #for x in cropped[:, 90]:
        #print(x)
        

    

