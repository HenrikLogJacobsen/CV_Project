from ultralytics import YOLO
import cv2
import os


source = 'output_video.mp4'
frame_size = (128,1024)
confidence = .2

# Pretrained YOLOv8n model
model = YOLO('yolov8n.pt')

# Setting detectable classes
with open('data/names.txt', 'r') as f:
    target_classes = [line.strip() for line in f]

classes = []
for key, value in model.names.items():
    if value in target_classes:
        classes.append(key)

# NOTE: Scooter and rider class missing

# Inference
results = model(
    source=source,
    conf=confidence,
    imgsz=frame_size, 
    save=True, 
    #save_txt=True, # includes BB labes
    classes=classes,
    stream=True
)

for result in results:
    pass