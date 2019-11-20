import os
import cv2
from PIL import Image

# change the picture brightness
def brightness(img_dir):
    for image_path in os.listdir(img_dir):
        image_path_dir = os.path.join(img_dir, image_path)
        img = Image.open(image_path_dir)
        img = img.point(lambda p:p*2)
        img.save('bright'+image_path)

# image resize
def image_resize(img_dir):
    for image_path in os.listdir(img_dir):
        image_path_dir = os.path.join(img_dir, image_path)
        img = Image.open(image_path_dir)
        img = img.resize((112, 112), Image.ANTIALIAS)
        img.save(os.path.join(img_dir, image_path))


