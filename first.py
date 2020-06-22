import numpy as np

import cv2

# img = np.zeros((400,400,1), np.uint8)

img = cv2.imread("hello.jpg")
cv2.line(img , (300,300) , (500,750), (0,0,0), 2)
# cv2.rectangle(img , (100,100) , (200,200), (255,100,255), 2)
cv2.imshow("my_img1" , img)



cv2.waitKey(0)

cv2.destroyAllWindows()

