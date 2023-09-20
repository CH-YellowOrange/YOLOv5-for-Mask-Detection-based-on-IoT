import cv2
import time
import numpy as np
from yolo import YOLO
from PIL import Image

def detect_image(image_path):
    print('Start detect!')
    yolo = YOLO()
    try:
        image = Image.open(image_path)
    except:
        print('Open Error! Try again!')
        pass
    else:
        r_image = yolo.detect_image(image)
        r_image.save(image_path.split('.')[0] + '_result.png')
    print('Finish detect!')

detect_image('D:/MaskDetect-YOLOv4-PyTorch-master/MaskDetect-YOLOv4-PyTorch-master/1.png')
detect_image('D:/MaskDetect-YOLOv4-PyTorch-master/MaskDetect-YOLOv4-PyTorch-master/2.png')
detect_image('D:/MaskDetect-YOLOv4-PyTorch-master/MaskDetect-YOLOv4-PyTorch-master/3.png')
detect_image('D:/MaskDetect-YOLOv4-PyTorch-master/MaskDetect-YOLOv4-PyTorch-master/4.png')
detect_image('D:/MaskDetect-YOLOv4-PyTorch-master/MaskDetect-YOLOv4-PyTorch-master/5.png')
detect_image('D:/MaskDetect-YOLOv4-PyTorch-master/MaskDetect-YOLOv4-PyTorch-master/6.png')
detect_image('D:/MaskDetect-YOLOv4-PyTorch-master/MaskDetect-YOLOv4-PyTorch-master/7.png')
detect_image('D:/MaskDetect-YOLOv4-PyTorch-master/MaskDetect-YOLOv4-PyTorch-master/8.png')
detect_image('D:/MaskDetect-YOLOv4-PyTorch-master/MaskDetect-YOLOv4-PyTorch-master/9.png')
detect_image('D:/MaskDetect-YOLOv4-PyTorch-master/MaskDetect-YOLOv4-PyTorch-master/10.png')