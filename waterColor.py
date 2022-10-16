import cv2
img = cv2.imread('./assets/demo2.jpg')
res = cv2.stylization(img, sigma_s=60, sigma_r=0.6)

cv2.imwrite("waterColor.jpg",res)