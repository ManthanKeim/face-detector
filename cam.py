import numpy as np
import time
import cv2

# img = np.zeros((400,400,1), np.uint8)
cap = cv2.VideoCapture(0)

# count =0
while True :

# img = cv2.imread("hello.jpg")
    ret , img = cap.read()
# cv2.line(img , (300,300) , (500,750), (0,0,0), 2)
# cv2.rectangle(img , (100,100) , (200,200), (255,100,255), 2)
#     time.sleep(1)
    gray = cv2.cvtColor(img , 44)
    cv2.imshow("image" , gray)


    # cv2.imwrite("images/" + str(count) + "-image.jpg" , img)
    # count += 1
    cv2.waitKey(1)


# cv2.destroyAllWindows()

