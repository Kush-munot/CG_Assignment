import cv2

img = cv2.imread("./assets/demo2.jpg")
dst_gray, dst_color = cv2.pencilSketch(img, sigma_s=60, sigma_r=0.07, shade_factor=0.05) 
cv2.imwrite("psketch.jpg",dst_gray)
cv2.imwrite("csketch.jpg",dst_color)