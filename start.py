# import librarys
import numpy as np # i dont think i even use this at all
import cv2 # This is the library we will use to do things with the webcam and manipulate the image we get from it
#learning this library was a pain and I haven't been fully exposed to its capabilitys
import time # t i m e 
import os # system functions and stuff
import json

true = True
candlejson = "candle1.json"
#This was scrapped
#candlejson = input("Please give an empty or non-existent json file to push the final data to (ex: candle1.json) > ")
#def defineagain():
#        candlejson = input("Please re-read the input prompt (file was not empty) > ")
#
#def checkfile():
#    if os.path.getsize(candlejson) <= 0:
#        defineagain()
#with open(candlejson, 'r') as f: # run a check to see if the file the user inputed is empty, or not existing, and if it does, yell at them
#    defineagain()

cap = cv2.VideoCapture(1) # set our video capture device, or the webcam
count = 0
finaldata = {} # create an array that we can push to each minute.
timesran = -1
def onMouse(event, x, y, flags, param): # this entire function is to identify coordinates when you clicked inside the window
    if event == cv2.EVENT_LBUTTONDOWN: # if we detect that the left mouse was clicked
       print('x = %d, y = %d'%(x, y)) # print those coords where the mouse was clicked
cv2.setMouseCallback('cropped image with line', onMouse) # make sure the callback is set to the final window

while True: # run everything inside this codeblock endlessly until we encounter a break or interupt
    ret, frame = cap.read() #set the variables (not really variables but constants) to cap.read() meaning were reading the frames directly from the webcam

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # convert the image to grayscale
    ret,thresh1 = cv2.threshold(gray,140,255,cv2.THRESH_BINARY) #create a brightness threshhold so we can try to get only the candle and not the background
    cropped = thresh1[100:265, 180:350] #y, x format : pt1:x272:y100,  pt2:x350:y200 # crop the image so its a smaller picture to mess with


    
    #cv2.imshow('original', frame) #Create the window with the original image
    #cv2.imshow('#1 grayscale image', gray) #Create a window with the grayscaled image
    #cv2.imshow('#2 grayscale with threshold', thresh1) #Create a window with the grayscaled image and a threshold for brightness
    #cv2.imshow('#3 cropped image', cropped) #Create a window with the cropped images of both the grayscale and threshold
        
    croplines = cv2.cvtColor(cropped, cv2.COLOR_GRAY2BGR) # Take the Cropped image and convert it back to full color so we can draw lines over it
    croplines1 = cv2.line(croplines, (110, 0), (110, 272), (0, 0, 255)) # Draw a red line from top to bottom #B, G, R because REASONS # also in x, y format
    croppedwithlines = cv2.line(croplines1, (0, 155), (250, 155), (0, 255, 0)) # Draw a green line from left to right # B, G, R because REASONS # also in x, y format
    
    cv2.imshow('cropped image with line', croppedwithlines) # send the image to a window # this is the only window we need right now
    cv2.setMouseCallback('cropped image with line', onMouse)
    #print("Pass")

    
    
    if cv2.waitKey(20) & 0xFF == ord('q'): # If the user hits Q on the keyboard, break the loop and stop the script
        break

    for x in cropped[:, 110]: #scan through all the pixels in the highlighted red column
       if x == 255: # If we detect a lit pixel
                count +=1

    timesran +=1
    timesranstring = str(timesran) + "m"

    count -=10 # Subtract 10 from the final count value so its the floor where the green line is
    #print(count) 
    finaldata.update({timesranstring:count})
    print(finaldata)
    count = 0               

    #time.sleep(1)
    if timesran == 99999999999999999999:
        #Place in a function that pushes the finaldata array to a .json file
        
        with open(candlejson, 'w') as f:
            json.dump(finaldata, f, sort_keys=True, indent=4)  # write back to file
        break

    