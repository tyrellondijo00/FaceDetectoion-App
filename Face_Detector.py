import cv2

trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') #Load some pretrained data on face frontals from opencv (haar cascade algorithm)

#Capture Video from webcam
webcam = cv2.VideoCapture(0)

#Iterate over frames forever
while True:
    #Read the current frame
    successful_frame_read, frame = webcam.read()

    grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #Make the image grayscale for the algorithm

    face_coordinates = trained_face_data.detectMultiScale(grayscaled_img) #Detect the faces

    #Draw squares on faces
    for (x, y, w, h) in face_coordinates:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 2)

    cv2.imshow('Tyrells Face Detector', frame) #Clever Programmer Face Detector is the name of the window that pops up

    key = cv2.waitKey(1) #Makes the program to not instatntly close

    #Stop if q is pressed
    if key ==81 or key==113:
        break

webcam.release()

print("Code Completed")