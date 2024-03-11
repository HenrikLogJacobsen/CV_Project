from ultralytics import YOLO

# Pretrained YOLOv8n model
model = YOLO('yolov8n.pt')

# Inference
results = model(source='test.mp4', show=True, save=True)