# Project

## Short Project description
This final project challenges you to apply your computer vision knowledge to solve a real-world problem. Choose from four exciting tracks:  tracking for analyzing sports performance, 3D medical image segmentation to aid in diagnosis, exploring object detection for autonomous driving or getting creative with generative models in compute vision.

## Task: Object Detection with LiDAR Data from Trondheim
Navigate the complexities of real-time perception for autonomous vehicles. In this track you will work
on a LiDAR dataset collected by the NAPLab at NTNU. Your task here is to perform object detection
for 8 classes.

- Dataset: You’ll utilize local LiDAR data from captured in Trondheim around Gløshaugen campus.
This data is extracted as grayscale images in png format. There are 8 bounding box classes in the
accompanying labels, in the YOLO v1.1 format.

## Tips from project description
- <b>Performance Metrics:</b> We expect you to at least measure the COCO mAP@0.5:0.95 metric in
addition to inference speed.

- <b>Recommended Loss Function:</b> Cross-entropy loss is a common choice for multi-class segmen-
tation tasks in autonomous driving, aiming to correctly classify each pixel in the image.

# TODO:
- Load in data
- Experiment with Ultralytics