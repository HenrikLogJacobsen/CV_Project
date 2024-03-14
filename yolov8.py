from ultralytics import YOLO
import cv2



# Load in a sample image
image_sample = cv2.imread('data/images/frame_000000.PNG')
image_height, image_width, _ = image_sample.shape

# Pretrained YOLOv8n model
model = YOLO('yolov8n.pt')

# Inference
results = model(source='data/images/', conf=.4, imgsz=(image_height,image_width), save=True, save_txt=True)

