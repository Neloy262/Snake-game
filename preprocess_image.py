import cv2
import numpy as np
from PIL import Image


def process(image):
    image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
    image = cv2.flip(image, 1)
 
    image = cv2.resize(image,(84,84))

    return image




    
