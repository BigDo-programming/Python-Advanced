#  x Open for exclusive creation, failing if the file already exists.
# file = open("text-x.txt", "x")


# w Creates a new file for writing. Overwrites the file if the file exists.
# file = open("text-w.txt", "w")


def write_to_file(file_path, mode, text):
    file = open(file_path, mode)
    file.write(text)
    file.close()


write_to_file("numbers.txt", "w", """1
2
3
4
5
6
""")


# a  Creates a new file - if the file does not exist, or append to exist.
# file = open("text-a.txt", "a")

def write_to_file(file_path, mode, text):
    with open(file_path, mode) as file:
        file.write(text)


data = 'I just created my first file!'
write_to_file("my_first_file.txt", "a", data)


