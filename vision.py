import io 
import os
# Imports the Google cloud client libary
from google.cloud import vision
from google.cloud.vision import types

os.environ['GOOGLE_APPLICATION_CREDENTIALS']=r'ServiceAccountToken.json'

# Instantieates a clinet
client = vision.ImageAnnotatorClient()
# print(dir(client))

# The name of the image file to annotate
file_name= os.path.abspath('image.jpg')

# Loads the image into memory
with io.open(file_name,'rb') as image_file:
    content= image_file.read()
image= vision.types.Image(content=content)

# Performs lable detetion on the image file 
respose=client.text_detection(image=image)
# labels=respose.label_annotations

# print("********************TEXT*****************")
# for text in tex
print(respose)