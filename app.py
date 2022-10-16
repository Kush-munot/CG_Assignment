from turtle import color
import cv2
import urllib.request
import skimage 
from skimage.io import imread
from skimage.data import coffee,camera
from skimage.filters import gaussian,roberts
import numpy as np

def img_to_gray(url,file_path,file_name):
    full_path=file_path+file_name
    tr=imread(full_path)
    cv2.imwrite("cartoon.jpg",cmap='gray')
    gray=contour(np.flipud(tr),color='k',levels=np.linspace(-10,100,3))
    cv2.imwrite('gray.jpg',gray)

def img_to_cartoon(url,file_path,file_name):
    full_path=file_path+file_name
    tr=imread(full_path)
    cartoon=(contour(np.flipud(tr),colors='k',levels=np.linspace(-10,100,3)))
    cv2.imwrite('gray.jpg',cartoon)

def img_to_blue(url,file_path,file_name):
    full_path=file_path+file_name
    tr=imread(full_path)
    blue=(contourf(np.flipud(tr),levels=np.linspace(-10,100,3),cmap='Blues'))
    cv2.imwrite('gray.jpg',blue)
    savefig('./images/blue.png')
    
def img_to_inferno(url,file_path,file_name):
    full_path=file_path+file_name
    tr=imread(full_path)
    inferno=(contourf(np.flipud(tr),levels=3,cmap='inferno'))
    cv2.imwrite('gray.jpg',inferno)
    savefig('./images/inferno.png')
    
def img_to_blur(url,file_path,file_name):
    full_path=file_path+file_name
    tr=imread(full_path)
    blur=gaussian(tr,sigma=10,multichannel=True)
    cv2.imwrite('gray.jpg',blur)

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
