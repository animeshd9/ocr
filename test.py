# import cv2
# # def thresholding(image):
# #     return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
# img =cv2.imread("image.jpg")
# img = cv2.resize(img, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC)
# img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# # img = cv2.threshold(img, 65, 255, cv2.THRESH_BINARY)[1] 
# # # img=  cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
# # cv2.imshow('img',img)
# # cv2.waitKey(0)
# ret,thresh1 = cv2.threshold(img,150,255,cv2.THRESH_BINARY)
# cv2.imshow('gray',thresh1)
# cv2.waitKey(0)import pytesseract
from pytesseract import Output
import cv2

img = cv2.imread('image.jpg')
d = pytesseract.image_to_data(img, output_type=Output.DICT)
n_boxes = len(d['level'])
for i in range(n_boxes):
	(x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])    
    img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)

cv2.imshow(img,'img')