import os
from os import path


def write_to_file(file_path, mode, text):
    with open(file_path, mode) as file:
        file.write(text)


data = 'I just created my first file!'
write_to_file("my_first_file.txt", "a", data)


if path.exists("my_first_file.txt"):
    os.remove("my_first_file.txt")
    print("File already deleted!")
