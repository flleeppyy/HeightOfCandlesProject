# import librarys
import numpy as np # i dont think i even use this at all
import cv2 # This is the library we will use to do things with the webcam and manipulate the image we get from it
#learning this library was a pain and I haven't been fully exposed to its capabilitys
import time # t i m e 

cap = cv2.VideoCapture(1) # set our video capture device, or the webcam
count = 0
finaldata = [] # create an array that we can push to each minute.
timesran = 0
def onMouse(event, x, y, flags, param): # this entire function is to identify coordinates when you clicked inside the window
    if event == cv2.EVENT_LBUTTONDOWN: # if we detect that the left mouse was clicked
       print('x = %d, y = %d'%(x, y)) # print those coords where the mouse was clicked
cv2.setMouseCallback('cropped image with line', onMouse) # make sure the callback is set to the final window

while True: # run everything inside this codeblock endlessly until we encounter a break or interupt
    ret, frame = cap.read() #set the variables (not really variables but constants) to cap.read() meaning were reading the frames directly from the webcam

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # convert the image to grayscale
    ret,thresh1 = cv2.threshold(gray,140,255,cv2.THRESH_BINARY) #create a brightness threshhold so we can try to get only the candle and not the background
    cropped = thresh1[100:265, 180:350] #y, x format : pt1:x272:y100,  pt2:x350:y200 # crop the image so its a smaller picture to mess with


    
    cv2.imshow('original', frame) #create a window with the frames being processed
    cv2.imshow('#1 grayscale image', gray) #create a window with the frames being processed
    cv2.imshow('#2 grayscale with threshold', thresh1) 
    cv2.imshow('#3 cropped image', cropped) 

    
    croplines = cv2.cvtColor(cropped, cv2.COLOR_GRAY2BGR) # Take the Cropped image and convert it back to full color so we can draw lines over it
    croplines1 = cv2.line(croplines, (110, 0), (110, 272), (0, 0, 255)) # Draw a red line from top to bottom #B, G, R because REASONS # also in x, y format
    croppedwithlines = cv2.line(croplines1, (0, 155), (250, 155), (0, 255, 0)) # Draw a green line from left to right # B, G, R because REASONS # also in x, y format
    cv2.imshow('cropped image with line', croppedwithlines) # send the image to a window
    cv2.setMouseCallback('cropped image with line', onMouse)
    #print("Pass")

    
    
    if cv2.waitKey(20) & 0xFF == ord('q'): # If the user hits Q on the keyboard, break the loop and stop the script
        break

    for x in cropped[:, 110]: #scan through all the pixels in the highlighted red column
       if x == 255: # If we detect a lit pixel
                count +=1

    count -=10 # Subtract 10 from the final count value so its the floor where the green line is
    print(count) 
    finaldata.append(count)
    print(finaldata)
    count = 0                
                
        #165 - 10
        #print(x)
    
    timesran +=1
    timesranstring = str(timesran) + "m"
    #time.sleep(60)
    #if timesran == 13:
        # Place in a function that pushes the finaldata array to a .json file
        #break

    