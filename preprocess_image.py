import cv2
import numpy as np
from PIL import Image

def process(image):
    image = cv2.rotate(image, cv2.cv2.ROTATE_90_CLOCKWISE)
    image = cv2.flip(image, 1)
    im = Image.fromarray(image)
    im.save("Before.jpeg")
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = cv2.resize(image,(84,84))

    im = Image.fromarray(image)
    im.save("After.jpeg")
    image = np.expand_dims(image,axis=-1)
    

    return image

    
