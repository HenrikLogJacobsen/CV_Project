import os

def read_file(path):
    with open(path, "r") as file:
        file_contents = file.read()

    return file_contents
