import numpy as np
import time
import cv2

# img = np.zeros((400,400,1), np.uint8)
cap = cv2.VideoCapture(0)
face_detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

eyes_detectpr = cv2.CascadeClassifier("haarcascade_eye.xml")
# count =0
while True :

# img = cv2.imread("hello.jpg")
    ret , img = cap.read()
# cv2.line(img , (300,300) , (500,750), (0,0,0), 2)
# cv2.rectangle(img , (100,100) , (200,200), (255,100,255), 2)
#     time.sleep(1)
    gray = cv2.cvtColor(img , 7)
    faces = face_detector.detectMultiScale(gray , 2 , 5)
    eyes = eyes_detectpr.detectMultiScale(gray , 2 , 5 )

    for(x,y,w,h) in eyes :
        cv2.rectangle(img , (x,y) , (x+w,y+h) , (10,10 ,255) , 2)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (142, 32, 255), 4)


    for (x, y, w, h) in eyes:
        (x, y, w, h) = eyes[0]

        eye = img[y:y+h , x:x+w]


    # for(x,y,w,h) in faces :
    #     cv2.rectangle(img , (x,y) , (x+w,y+h) , (255,0,255) , 2)

    print(faces)
    print(eyes)

    # cv2.imshow("image" ,img)

    cv2.imshow("image", img)
    # cv2.imwrite("images/" + str(count) + "-image.jpg" , img)
    # count += 1
    cv2.waitKey(1)


# cv2.destroyAllWindows()

