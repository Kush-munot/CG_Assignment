import cv2
import numpy as np


def image_to_sketch():
    image = cv2.imread("./assets/demo2.jpg")

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

def image_to_oilPaint():
    img = cv2.imread('./assets/demo2.jpg')
    res = cv2.xphoto.oilPainting(img, 7, 1)
    cv2.imwrite("oilPaint.jpg",res)
    
def image_to_colorSketch():
    img = cv2.imread("./assets/demo2.jpg")
    dst_gray,dst_color = cv2.pencilSketch(img, sigma_s=60, sigma_r=0.07, shade_factor=0.05) 

    cv2.imwrite("csketch.jpg",dst_color)
    
def image_to_darkSketch():
    img = cv2.imread("./assets/demo2.jpg")
    dst_gray,dst_color = cv2.pencilSketch(img, sigma_s=60, sigma_r=0.07, shade_factor=0.05) 

    cv2.imwrite("psketch.jpg",dst_gray)
    
def image_to_waterColor():
    import cv2
    img = cv2.imread('./assets/demo2.jpg')
    res = cv2.stylization(img, sigma_s=60, sigma_r=0.6)

    cv2.imwrite("waterColor.jpg",res)
    
def image_addition():
    image1 = cv2.imread('./assets/demo4.jpg')
    image2 = cv2.imread('./assets/demo3.jpg')
    weightedSum = cv2.addWeighted(image1, 0.5, image2, 0.4, 0)
    cv2.imwrite('weighted_image.jpg', weightedSum)
    
def image_subtraction():
    image1 = cv2.imread('./assets/demo3.jpg')
    image2 = cv2.imread('./assets/demo4.jpg')
    subtract = cv2.subtract(image1, image2)
    cv2.imwrite('subtract.jpg', subtract)

def bgr_hsv():
    image = cv2.imread("./assets/demo2.jpg")

    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    cv2.imwrite('hsv.jpg', hsv)
    
def smooth_image():
    image = cv2.imread("./assets/demo4.jpg")

    deionize = cv2.fastNlMeansDenoisingColored(image, None, 10, 10, 7, 15)
    cv2.imwrite('deionize.jpg', deionize)
    
def image_translation():
    image = cv2.imread("./assets/demo4.jpg")
    height, width = image.shape[:2]
    quarter_height, quarter_width = height / 4, width / 4
    T = np.float32([[1, 0, quarter_width], [0, 1, quarter_height]])
    img_translation = cv2.warpAffine(image, T, (width, height))
    cv2.imwrite('translation.jpg', img_translation)
    
def bilateral_filter():
    image = cv2.imread("./assets/demo4.jpg")
    
    b_filter = cv2.bilateralFilter(image,9,95,95) 
    cv2.imwrite('bilateralFilter.jpg', b_filter)
    


if __name__=="__main__":
    # image_to_sketch()
    # image_to_oilPaint()
    # image_to_colorSketch()
    # image_to_darkSketch()
    # image_to_waterColor()
    # image_addition()
    # image_subtraction()
    # bgr_hsv()
    # smooth_image()
    # image_translation()
    # bilateral_filter()
    print("Computer Graphics TA 1 ---- Group 1")
    

    while(1):
        print("Choices Available are : ")
        print("1.   Image to Sketch")
        print("2.   Image to Oil Paint")
        print("3.   Image to Color Sketch")
        print("4.   Image to Dark Sketch")
        print("5.   Image to Water Color")
        print("6.   Image Addition")
        print("7.   Image Subtraction")
        print("8.   Get Hue Saturation Value")
        print("9.   Smooth Image")
        print("10.  Image Translation")
        print("11.  Bilateral Image Filter")
        print("0.   Exit")
        
        print("\n\n\n")
        
        opt = int(input("Enter Your Choice"))
        
        match opt:
            case 1:
                image_to_sketch()
                print("1")

            case 2:
                image_to_oilPaint()
                print("2")
            
            case 3:
                image_to_colorSketch()
                print("3")

            case 4:
                image_to_darkSketch()
                print("4")

            case 5:
                image_to_waterColor()
                print("5")

            case 6:
                image_addition()
                print("6")
            
            case 7:
                image_subtraction()
                print("7")
            
            case 8:
                bgr_hsv()
                print("8")
            
            case 9:
                smooth_image()
                print("9")
            
            case 10:
                image_translation()
                print("10")
            
            case 11:
                bilateral_filter()
                print("11")
                
            case _:
                print("default")