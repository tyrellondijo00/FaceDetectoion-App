import cv2

trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') #Load some pretrained data on face frontals from opencv (haar cascade algorithm)

#Choose Image To Detect Faces in. imRead means image read
#img = cv2.imread('RDJ.jpg') 

#Capture Video from webcam
webcam = cv2.VideoCapture(0)

#Iterate over frames forever
while True:
    #Read the current frame
    successful_frame_read, frame = webcam.read()

grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #Make the image grayscale for the algorithm

cv2.imshow('Clever Programmer Face Detector', grayscaled_img) #Clever Programmer Face Detector is the name of the window that pops up

cv2.waitKey(1)#Makes the program to not instatntly close

"""
face_coordinates = trained_face_data.detectMultiScale(grayscaled_img) #Detect the faces

#Draw squares on faces
for (x, y, w, h) in face_coordinates:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0,255,0), 2)


cv2.imshow('Clever Programmer Face Detector', img) #Clever Programmer Face Detector is the name of the window that pops up

cv2.waitKey()#Makes the program to not instatntly close
"""

print("Code Completed")