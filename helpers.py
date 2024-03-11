import os

def read_file(path):
    file_path = get_path(path)

    with open(file_path, "r") as file:
        file_contents = file.read()

    return file_contents

def get_path(path):
    return os.path.join("/datasets/tdt4265/ad/NAPLab-LiDAR", path)
