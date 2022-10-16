import cv2
import urllib.request

def image_to_sketch():
    image = cv2.imread("./assets/demo.jpg")

    grey_filter = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imwrite("graysacle.jpg",grey_filter)

    invert = cv2.bitwise_not(grey_filter)
    cv2.imwrite("invert.jpg",invert)

    blur = cv2.GaussianBlur(invert,(21,21),0)
    cv2.imwrite("blur.jpg",blur)

    invertedBlur = cv2.bitwise_not(blur)
    cv2.imwrite("invBlur.jpg",invertedBlur)

    sketch = cv2.divide(grey_filter,invertedBlur,scale=256.0)
    cv2.imwrite("sketch.jpg",sketch)


def dl_jpg (url, file_path, file_name):
    full_path = file_path + file_name + '.jpg'
    urllib.request.urlretrieve(url, full_path)
    
url=input('Enter img URL to download: ')
file_name = input('Enter file name to save as: ')
dl_jpg(url, 'images/', file_name)
