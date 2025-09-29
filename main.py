#import the open cv package
import cv2 as cv

#use the camera that you want to capture (most likely 0 or 1)
cap = cv.VideoCapture(0)
#put the path of the downlaoded Haarcascade inside the brackets
cascade = cv.CascadeClassifier('haarcasc.xml')

#if camera is not found it shows us 
if not cap.isOpened():
    print("camera not found")
    exit()

#if there is a problem with the HAARCASCADE Path it will show us
if cascade.empty():
    print("HAARCASCADE Path not found or issue with the path")
    exit()

#we use a while loop to track the face permanently
while True:
    #we read in the img with cap.read() 
    success, img = cap.read()
    
    #we need to convert the color to gray because its better for haarcascade
    img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    #the tracked faces are saved in the faces variable, it is a list
    faces = cascade.detectMultiScale(img_gray)

    #for loop to put the rectangle; 
    for x, y, width, height in faces:
        #we put the cv.rectangle method to put a rectangle around the tracked face
        cv.rectangle(img, (x,y), (x + width, y + height), color=(0,0,255), thickness=5)
    
    #we display our image
    cv.imshow('img', img)

    #if you press q the tracking get closed
    if cv.waitKey(1) == ord("q"):
        break
