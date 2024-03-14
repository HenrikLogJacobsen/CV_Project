import cv2
import os

# image_sample = cv2.imread('data/images/frame_000000.PNG')
# image_height, image_width, _ = image_sample.shape
image_shape = (128,1024)

# Get the list of image files in the directory
with open('data/train.txt', 'r') as file:
    image_files = [line.strip() for line in file if line.strip().endswith('.PNG')]

# Create a VideoWriter object
video_file = 'output_video.mp4'
fourcc = cv2.VideoWriter_fourcc(*'mp4v')

video_writer = cv2.VideoWriter(video_file, fourcc, 30, image_shape)

# Iterate over the image files and write each frame to the video
for image_file in image_files:
    image_path = os.path.join('data/', image_file)
    frame = cv2.imread(image_path)
    video_writer.write(frame)

# Release the VideoWriter object
video_writer.release()