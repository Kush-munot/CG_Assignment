import cv2
# import urllib.request


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



# def dl_jpg (url, file_path, file_name):
#     full_path = file_path + file_name + '.jpg'
#     urllib.request.urlretrieve(url, full_path)
    






# if __name__ == "__main__":
    # url=input('Enter img URL to download: ')
    # file_name = "demo"
    # dl_jpg(url, 'assets/', file_name)