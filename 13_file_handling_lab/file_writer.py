#  x Open for exclusive creation, failing if the file already exists.
# file = open("text.txt-x", "x")

def write_to_file(file_path, mode, text):
    file = open("text.txt-w", "w")
    file.write(text)


write_to_file("numbers.txt", "w", """1
2
3
4
5
6
""")

# w Creates a new file for writing. Overwrites the file if the file exists.
# file = open("text.txt-w", "w")
#
# a  Creates a new file - if the file does not exist, or append to exist.
# file = open("text.txt-a", "a")
