import os

def read_file(path):
    file_path = os.path.join("/datasets/tdt4265/ad/NAPLab-LiDAR", path)

    with open(file_path, "r") as file:
        file_contents = file.read()

    return file_contents