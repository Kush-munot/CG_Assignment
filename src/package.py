import cv2
import numpy as np


def image_to_sketch(image_path):
    image = cv2.imread(image_path)

    grey_filter = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # cv2.imwrite("graysacle.jpg",grey_filter)

    invert = cv2.bitwise_not(grey_filter)
    # cv2.imwrite("invert.jpg",invert)

    blur = cv2.GaussianBlur(invert,(21,21),0)
    # cv2.imwrite("blur.jpg",blur)

    invertedBlur = cv2.bitwise_not(blur)
    # cv2.imwrite("invBlur.jpg",invertedBlur)

    sketch = cv2.divide(grey_filter,invertedBlur,scale=256.0)
    cv2.imwrite("sketch.jpg",sketch)

def image_to_oilPaint(image_path):
    img = cv2.imread(image_path)
    res = cv2.xphoto.oilPainting(img, 7, 1)
    cv2.imwrite("oilPaint.jpg",res)
    
def image_to_colorSketch(image_path):
    img = cv2.imread(image_path)
    dst_gray,dst_color = cv2.pencilSketch(img, sigma_s=60, sigma_r=0.07, shade_factor=0.05) 

    cv2.imwrite("csketch.jpg",dst_color)
    
def image_to_darkSketch(image_path):
    img = cv2.imread(image_path)
    dst_gray,dst_color = cv2.pencilSketch(img, sigma_s=60, sigma_r=0.07, shade_factor=0.05) 

    cv2.imwrite("psketch.jpg",dst_gray)
    
def image_to_waterColor(image_path):
    img = cv2.imread(image_path)
    res = cv2.stylization(img, sigma_s=60, sigma_r=0.6)
    cv2.imwrite("waterColor.jpg",res)
    
def image_addition(image1_path, image2_path):
    image1 = cv2.imread(image1_path)
    image2 = cv2.imread(image2_path)
    weightedSum = cv2.addWeighted(image1, 0.5, image2, 0.4, 0)
    cv2.imwrite('weighted_image.jpg', weightedSum)
    
def image_subtraction(image1_path, image2_path):
    image1 = cv2.imread(image1_path)
    image2 = cv2.imread(image2_path)
    subtract = cv2.subtract(image1, image2)
    cv2.imwrite('subtract.jpg', subtract)

def bgr_hsv(image_path):
    image = cv2.imread(image_path)

    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    cv2.imwrite('hsv.jpg', hsv)
    
def smooth_image(image_path):
    image = cv2.imread(image_path)

    deionize = cv2.fastNlMeansDenoisingColored(image, None, 10, 10, 7, 15)
    cv2.imwrite('deionize.jpg', deionize)
    
def image_translation(image_path):
    image = cv2.imread(image_path)
    height, width = image.shape[:2]
    quarter_height, quarter_width = height / 4, width / 4
    T = np.float32([[1, 0, quarter_width], [0, 1, quarter_height]])
    img_translation = cv2.warpAffine(image, T, (width, height))
    cv2.imwrite('translation.jpg', img_translation)
    
def bilateral_filter(image_path):
    image = cv2.imread(image_path)
    
    b_filter = cv2.bilateralFilter(image,9,95,95) 
    cv2.imwrite('bilateralFilter.jpg', b_filter)