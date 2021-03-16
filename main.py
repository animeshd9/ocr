import cv2
import pytesseract 
from pytesseract import Output
from PIL import Image
import json

# def resacle(image):
#     return cv2.resize(img, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC)


img =cv2.imread("cs3.jpg")
# img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.resize(img, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC)
# # # ret,thresh1 = cv2.threshold(img,150,255,cv2.THRESH_BINARY)

# img = cv2.threshold(img, 0,255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
d = pytesseract.image_to_string(img)

h, w,  c = img.shape
boxes = pytesseract.image_to_boxes(img) 
for b in boxes.splitlines():
    b = b.split(' ')
    img = cv2.rectangle(img, (int(b[1]), h - int(b[2])), (int(b[3]), h - int(b[4])), (0, 255, 0), 2)
# d = pytesseract.image_to_string(img)
# print(d.keys())
# data_json=json.dumps(d["text"])
# print(data_json)
print(d)
# n_boxes = len(d['text'])
# for i in range(n_boxes):
#     if int(d['conf'][i]) > 60:
#         (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
#         img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
# cv2.imshow('gray',thresh1)
cv2.imshow('img', img)
cv2.waitKey(0)
# img=Image.open("Happy.jpg")
# d = pytesseract.image_to_string(img)
# print(d)