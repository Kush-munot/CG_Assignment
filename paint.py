import cv2

img = cv2.imread('./assets/demo2.jpg')
res = cv2.xphoto.oilPainting(img, 7, 1)
cv2.imwrite("oilPaint.jpg",res)