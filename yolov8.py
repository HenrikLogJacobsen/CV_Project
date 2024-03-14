from ultralytics import YOLO
import cv2
import os


image_shape = (128,1024)
source = 'output_video.mp4'

# Pretrained YOLOv8n model
model = YOLO('yolov8n.pt')

# Setting detectable classes
with open('data/names.txt', 'r') as f:
    classes = [line.strip() for line in f]

# Set the class filter

# Inference
results = model(source=source, conf=.4, imgsz=image_shape, save=True, save_txt=True, classes=classes, stream=True)

